# NCAA D1 Men's Basketball Predctions
A project to attempt predicting the winning team of NCAA Division I Men's Basketball games.

See blog post here: (pending)
---
## Repo Layout
- README.md
- code
 - NCAA_Notebook.ipynb <-- Where I conducted all EDA, feature engineering, and modeling
 - NCAA_Scraper.ipynb <-- A collection of the scraper code implemented for acquiring data
 - graveyard <-- Directory of superceded files
  - NCAA_AWS_calc.ipynb <-- An attempt at hosting a computationally intensive step on AWS. An alternate strategy was implemented
  - NCAA_AWS_calc.py <-- .py version of the file above
  - NCAA-Notebook_superceded.ipynb <-- An attempt at first predicting player-by-player and then team-by-team scores per game event. Proved to be very difficult, with disappointing results. 
  - data
   - player_boxscores_df.csv <-- Produced from play_boxscores directory
   - myteam_ewm_df.csv <-- Produced from myteam_ewm directory
   - yourteam_ewm_df.csv <-- Produced from yourteam_ewm directory
   - joined_modeling.csv <-- Final dataframe prepared for modeling
   - point_spread_history.csv <-- Scraped from here: https://www.teamrankings.com/ncb/odds-history/win/
   - schools.csv <-- Scraped on a year-to-year basis from here: https://www.sports-reference.com/cbb/seasons/2018-school-stats.html
   - player_ewm_df.csv <-- Superceded, produced from player_ewm directory
   - player_boxscores <-- files in this directory were scraped with NCAA_Scraper.ipynb
   - myteam_ewm <-- files in this directory are rolling stats generated from the NCAA_Notebook
   - yourteam_ewm <-- files in this directory are rolling stats generate from the NCAA_notebook
   - polls_rank <-- files in this directory were scraped from here on a year-by-year basis: https://www.sports-reference.com/cbb/seasons/2018-polls.html