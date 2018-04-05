# Predicting NCAA Division 1 Men's Basketball Game Outcomes
#### By: Tucker Allen
#### Date: April 5, 2017

## Introduction

/t In the United States, if you want to place a wager on professional or collegiate sports, you have to locate yourself within the borders of Nevada. Nevada has ultimately held a monopoly over the sports wagering industry within the U.S., having been the only state protected from the rules imposed by the Professional and Amateur Sports Protection Act (PASPA) of 1992. PASPA, which outlawed sports wagering at the federal level, was introduced in an effort to maintain the integrity of professional and collegiate sports by eliminating any financial incentive for referees to unfairly officiate, or for players to intentionally underperform. The passing of PASPA was most fervently spearheaded by the professional and collegiate sports associations themselves, such as the NCAA and the NBA, so that fans and customers would not lose trust in the game. Recently, that fervor has waned, with the NBA and NHL leaders seeming more complacent to the idea of reintroducing widespread sports wagering. This has led NJ Governor Chris Christie, having identified an opportunity to revitalize the crumbling Atlantic City boardwalk with the introduction of sports wagering, to initiate Christie v. NCAA in 2017. With the case now in front of the Supreme Court, and a ruling expected as early as July, an overturning of PASPA could open the floodgates for what some have estimated could be a $6b U.S. industry.

\t If sports wagering opportunities suddenly grow from one state, to fifty states, there will doubtlessly be immense growth in the both the bettors base, and betting houses, eager to be first-movers in the new space. There will also be tremendous opportunity for information/modeling middleman companies to provide this new, broad bettors base with fee-based tools and subscriptions. Numerous companies already occupy this space, with varying success, at a much smaller scale because betting has since been limited to the state of Nevada. As a proof-of-concept in prediction-modeling services, I elected to investigate prediction modeling for NCAA Men’s Basketball games.

---

## The Data

### What Didn’t Work

I began by scraping player-by-player boxscores for every Division 1 Men’s college basketball game that has taken place since the 2011 season, resulting in approximately 870,000 rows of data. Rather than approach the problem as a classification (1/0 for W/L) problem at first, I tried to instead predict, more granularly, the amount of points scored by every individual player on a given team, on a given night. Ideally, if one could accurately predict individual player scores, you could simply combine them to get a team score, and compare team scores to get an accurate winner. This strategy proved to be uniquely difficult because of the tremendous variance in player usage on any given game night. A player can only score points if he is in the game, and the minutes played (mp) by all players varied wildly from game to game, dictated by the whims of the coach. To really predict the points scored by a player, accurately, would mean accurately predicting the “mp” of that player for a given night, which is a monumental task outside the resource scope of this project.

Next, I elected to explore predicting a teams final score, since every team plays the exact same amount of minutes, eliminating the minutes-played variance. This proved more feasible, but generally elicited cross-validated accuracy scores around 0.41, when used to predict the winning team of game events. 

### What Did Work

Finally, I explored explicitly predicting the winning team of a game event on a classification basis. Before engineering additional features, this strategy appeared to yield better accuracy results (~60%).

### The Process

- Glossary:
 - TOI: Team-of-interest (The team being predicted for success/win/1 or failure/loss/0)
 - OPP: Opponent (The team opposing the TOI)
 - SOS: Strength of Schedule
 - SRS: Simple Rating System 

Firstly, I collected over 870,000 rows of player-by-player box scores from https://www.basketball-reference.com/. The scraping was done by leveraging Python requests of the play-index URL, parsing the page information with BeautifulSoup, appending the information to a DataFrame, cycling the URL to the next page and then repeating the process, until every player box score since the 2011 season was aggregated. The process yielded a final aggregated .csv file of approximately 100Mb. 

Next, I collapsed the player box scores into team box scores by applying a ‘group_by’ and summation on a Date/School/Opponent index. This yielded approximately 87,000 game events, with each observation including the TOI, the boxscore for the TOI, and the OPP.

Next, for every game event, I wanted to get an informative cross-section of previous performances of the given team. I accomplished this by producing exponentially weighted means of several decay rates, and also rolling means of 30 games (approximate length of 1 season) applied to each TOI’s box score statistics. This strategy aimed to provide information that was both “recently” and more “distantly” weighted. These weighted means and rolling means were ‘shifted’ by one row, so that the production of that particular game being predicted on was not included in the available information. This same process was applied to the OPP, yielding “recent” and more “distant” information again about how many pts/rebounds/etc. that team typically holds previous TOIs to. Appending all of this information as features aims to inform the model of the typical and recent variation in TOI performance, and also the the typical and recent variation in OPP defensive performance.

Next, I aimed to weight these performances of the TOI and OPP by including a “Strength of Schedule” (SOS). An SOS metric is a commonly used metric by sport statisticians, although the actual values for any given team at any given point varies from source to source. I utilized the SOS metrics calculated by https://www.basketball-reference.com/ so that I could expect a 1:1 match between school names to make for easier joining. This time, I scraped https://www.sports-reference.com/cbb/seasons/ by school name and year, leveraging URL requests, parsing through BeautifulSoup, appending to a dataframe, cycling through each school and each year since 2011. This process also yielded a SRS for each TOI, a rating maintained by basketball-reference which aims to take into account a team’s average point differential and strength of schedule.

### The Final Model

During model selection and tuning, I elected to conduct Principal Component Analysis on my features, and eliminate 150 of my 200 engineered features. A significant amount of my features were highly correlated, as expected, since many of them were created from temporal autocorrelations, and it was not particlarly necessary to maintain the interpretability of my final model coefficients.  A Logistic Regression model yielded my best prediction accuracy (72.5%), penalty = ‘L2’, C = 0.01, tol=1e-05.



