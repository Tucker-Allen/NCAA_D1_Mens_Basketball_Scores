# NCAA D1 Men's Basketball Predctions
A project to attempt predicting the winning team of NCAA Division I Men's Basketball games.

See blog post here: https://tucker-allen.github.io/NCAA_Basketball/

---
## Repo Layout

### Note: All .csv files have been added to the .gitignore file due to size constraints

- README.md
- code
  - NCAA_Notebook.ipynb <-- Where I conducted all EDA, feature engineering, and modeling
  - NCAA_Scraper.ipynb <-- A collection of the scraper code implemented for acquiring data
  - graveyard <-- Directory of superceded files
    - NCAA_AWS_calc.ipynb <-- An attempt at hosting a computationally intensive step on AWS. An alternate strategy was implemented
    - NCAA_AWS_calc.py <-- .py version of the file above
    - NCAA-Notebook_superceded.ipynb <-- An attempt at first predicting player-by-player and then team-by-team scores per game event. Proved to be very difficult, with disappointing results. 
- data
  - player_boxscores_df.csv <-- Produced from player_boxscores directory
  - myteam_ewm_df.csv <-- Produced from myteam_ewm directory
  - yourteam_ewm_df.csv <-- Produced from yourteam_ewm directory
  - joined_modeling.csv <-- Final dataframe prepared for modeling
  - point_spread_history.csv <-- Scraped from here: https://www.teamrankings.com/ncb/odds-history/win/
  - schools.csv <-- Scraped on a year-to-year basis from here: https://www.sports-reference.com/cbb/seasons/2018-school-stats.html
  - player_ewm_df.csv <-- Superceded, produced from player_ewm directory
  - player_ewm (1.5GB) <-- Superceded
  - player_boxscores (106MB) <-- files in this directory were scraped with NCAA_Scraper.ipynb
  - myteam_ewm (99MB) <-- files in this directory are rolling stats generated from the NCAA_Notebook
  - yourteam_ewm (99MB) <-- files in this directory are rolling stats generated from the NCAA_notebook
  - polls_rank (381kB) <-- files in this directory were scraped from here on a year-by-year basis: https://www.sports-reference.com/cbb/seasons/2018-polls.html
  - marchmadness_2018 (16kB) <-- files in this directory were scraped from here: https://www.sports-reference.com/cbb/play-index/tourney.cgi?request=1&match=single&year_min=2018&year_max=2018&seed_cmp=eq&opp_seed_cmp=eq&pts_diff_cmp=eq&order_by_single=date_game&order_by_combined=g
- technical_nb.md <-- Technical notebook of project and results

---

## Summary

