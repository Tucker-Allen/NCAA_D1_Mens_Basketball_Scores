# Predicting NCAA Division 1 Men's Basketball Game Outcomes
#### By: Tucker Allen
#### Date: April 5, 2017

## Introduction

In the United States, if you want to place a wager on professional or collegiate sports, you have to locate yourself within the state borders of Nevada. The Silver State has ultimately held a monopoly over the U.S. sports wagering industry since 1992, having been the only state exempt from the rules imposed by the Professional and Amateur Sports Protection Act (PASPA) enacted that year. This legislation, which outlawed sports wagering at the federal level, was introduced in an effort to maintain the integrity of professional and collegiate sports by eliminating financial incentive for referees to unfairly officiate, or for players to intentionally underperform. The passing of PASPA was most fervently spearheaded by the professional and collegiate sports associations themselves, such as the NCAA and the NBA, so that fans and customers would maintain trust in the game and the product. Recently, the fervor to restrict gambling has waned, with the NBA and NHL leaders more complacent to the idea of reintroducing widespread sports wagering. This led NJ Governor Chris Christie, having identified an opportunity to revitalize the crumbling Atlantic City boardwalk with the introduction of sports wagering, to initiate Christie v. NCAA in 2017. With the case now in front of the Supreme Court, and a ruling expected as early as July, an overturning of PASPA could open the floodgates for what some have estimated could be a $6b U.S. industry.

If sports wagering opportunities suddenly explode from one state to fifty, there will doubtlessly be immense growth in the both the bettors base and in new betting houses, eager to be first-movers in the new space. There will also be tremendous opportunity for information/modeling middleman companies to provide this new, broad bettors base with fee-based tools and prediction subscriptions. Numerous companies already occupy this space, with varying success, but at a much smaller scale since sport wagering has so far been limited to the state of Nevada. As a proof-of-concept to potentially provide those prediction-modeling services, I elected to investigate some prediction modeling techniques for NCAA Men’s Division 1 Basketball games.

---

## The Data

I began by scraping player-by-player boxscores for every Division 1 Men’s college basketball game that has taken place since the 2011 season, resulting in approximately 870,000 rows of data. The data was scraped from https://www.basketball-reference.com/, leveraging Python requests of the play-index URL, parsing the page information with BeautifulSoup, appending the information to a DataFrame, cycling the URL to the next page and then repeating the process, until every player box score since the 2011 season was aggregated. The process yielded a final aggregated '.csv' file of approximately 100Mb in size.

### What Didn’t Work

Rather than approach the problem as a classification (1/0 for W/L) problem at first, I tried to instead predict, more granularly, the amount of points scored by every individual player on a given team, on a given night. Ideally, if one could accurately predict individual player scores, you could simply combine them to get a team score, and compare team scores to get an accurate winner. This strategy proved to be uniquely difficult because of the tremendous variance in how many minutes a given player will play on any given game night. It was not unusual for a star player to play for 32 minutes one game, and then 8 minutes the next. A player can only score points if he is in the game, and the number of minutes played are dictated by coach strategy, which is, by its nature, always changing. To really predict the points scored by a player, accurately, would mean accurately predicting the number of minutes that player will play for a given night. This would mean accurately predicting how a coach plans to utilize each of his players, which is a monumental task outside the resource scope of this project.

With that in mind, I elected to next explore predicting a teams final score on the team-event level, since every team plays the same amount of minutes in total, eliminating the minutes-played variance that existed on the by-player level. This proved more feasible, but still generally elicited cross-validated accuracy scores around 0.41, when used to predict the winning team of game events.

Exploring the strengths of the above strategies are reserved future studies, and may be improved with additional features or model selection beyond the Linear Regression I conducted. 

### What Did Work

Finally, I explored explicitly predicting the winning team of a game event on a classification basis. Before engineering additional features beyond a team's average boxscores, this classification strategy appeared to yield better accuracy results (~60%), and so was pursued for the remainder of this project.

### The Process

_Glossary:_
 - TOI: Team-of-interest (The team being predicted for success/win/1 or failure/loss/0)
 - OPP: Opponent (The team opposing the TOI)
 - SOS: Strength of Schedule
 - SRS: Simple Rating System  

First, I collapsed the player box scores that I initially scraped into team box scores by applying a ‘group_by’ and summation on a Date/School/Opponent index. This yielded approximately 87,000 game events, with each observation including the TOI, the boxscore for the TOI, and the OPP.

Next, for every game event, I wanted to get an informative cross-section of previous performances of the TOI. I accomplished this by producing exponentially weighted means of several decay rates, and also rolling means of 30 games (the approximate length of 1 season) applied to each TOI’s box score statistics. This strategy aimed to provide information that was both “recently” and more “distantly” weighted. These weighted means and rolling means were ‘shifted’ by one row, so that the production of that particular game being predicted on was not included in the available information. This same process was applied to the OPP, yielding “recent” and more “distant” information again about how many pts/rebounds/etc. that team typically holds previous TOIs to. Appending all of this information as features aimed to inform the model of the typical and recent variation in TOI performance, and also the the typical and recent variation in OPP defensive performance.

Next, I aimed to weight these performances of the TOI and OPP by including a “Strength of Schedule” (SOS). An SOS metric is a commonly used metric by sport statisticians, although the actual values for any given team at any given time varies from source to source. I utilized the SOS metrics calculated by https://www.basketball-reference.com/ so that I could expect a 1:1 match between school names to make for easier joining. This time, I scraped https://www.sports-reference.com/cbb/seasons/ by school name and year, leveraging URL requests, parsing through BeautifulSoup, appending to a dataframe, and cycling through each school and each year since 2011. This process also yielded a "Simple Rating System" (SRS) score for each TOI, a rating maintained by basketball-reference which aims to take into account a team’s average point differential and strength of schedule. This SRS appeared to improve model performance, so was included in the final model features.

I additionally explored adding AP polling ranks and Coach polling ranks as features. These polling ranks are conducted weekly throughout the course of the season, and aim to rank the top 25 teams in the country. Because my model aimed to make predictions on 350 teams overall, including information about less than 10% of those teams did little to improve the model performance, so I elected to exclude them.

## The Final Model

During model selection and tuning, I elected to conduct Principal Component Analysis on my features, and eliminate 150 of my 200 engineered features. A significant amount of my features were highly correlated, as expected, since many of them were created from temporal autocorrelations, and it was not particlarly necessary to maintain the interpretability of my final model coefficients. In summary, a Logistic Regression model yielded my best prediction accuracy, at 72.5% (training set of 70% size, cross validated on 3-folds of training set). Applying this best-tuned model to my test-set yielded a 3-folds cross validation accuracy of 72.7%.

I consider this performance to be marketable, considering that Pinnacle, an on-line wagering site with game predictions that closely mirror that of Las Vegas, has performed at 74.3% accuracy since 2003.

## For The Future

Although I am satisfied with this model's performance, I believe that there is still room for substantial improvement. Improved performance could likely be achieved by including Home/Away informationn, since Vegas sportsbooks have historically assigned an underlying advantage to Home teams over Away teams. I believe it would also help to include some more granular player information that would be able to identify offensive/defensive player mismatches or exploitations. Team biological information may also provide useful, since it will allow the model to identify when individual team members might have a height/weight/strength advantage/disadvantage over the opponent.




