
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[28]:


df = pd.read_csv('./df_clean.csv')


# In[29]:


rolling_stats = ['gs', 'mp', 'fg2', 'fg2a', 'fg3', 'fg3a', 'ft', 'fta',
                 'orb', 'drb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts', 'game_score', 'W']

lookbacks = ['_3day_', '_10day_', '_30day_', '_60day_', '_90day_', '_120day_']

metrics = ['mean', 'median']


# In[30]:


all_rolling = []

for i in metrics:
    for j in lookbacks:
        for k in rolling_stats:
            all_rolling.append(i+j+k)


# In[31]:


all_rolling.extend(['player', 'date_game'])


# In[32]:


rolling_stats.append('date_game')


# In[33]:


players = df['player'].unique()


# In[34]:


rolling_df = pd.DataFrame(columns=all_rolling)


# In[35]:


df.set_index(['player', 'date_game'], drop=False, inplace=True)


# In[36]:


count = 0
for player in players:
    if count % 500 == 0:
        print('parsing...', count)
    player_df = df.loc[player][rolling_stats].sort_values('date_game')

    mean_3day = player_df.drop('date_game', axis=1).rolling(window=3, center=False, min_periods=1).mean()
    mean_10day = player_df.drop('date_game', axis=1).rolling(window=10, center=False, min_periods=1).mean()
    mean_30day = player_df.drop('date_game', axis=1).rolling(window=30, center=False, min_periods=1).mean()
    mean_60day = player_df.drop('date_game', axis=1).rolling(window=60, center=False, min_periods=1).mean()
    mean_90day = player_df.drop('date_game', axis=1).rolling(window=90, center=False, min_periods=1).mean()
    mean_120day = player_df.drop('date_game', axis=1).rolling(window=120, center=False, min_periods=1).mean()

    median_3day = player_df.drop('date_game', axis=1).rolling(window=3, center=False, min_periods=1).median()
    median_10day = player_df.drop('date_game', axis=1).rolling(window=10, center=False, min_periods=1).median()
    median_30day = player_df.drop('date_game', axis=1).rolling(window=30, center=False, min_periods=1).median()
    median_60day = player_df.drop('date_game', axis=1).rolling(window=60, center=False, min_periods=1).median()
    median_90day = player_df.drop('date_game', axis=1).rolling(window=90, center=False, min_periods=1).median()
    median_120day = player_df.drop('date_game', axis=1).rolling(window=120, center=False, min_periods=1).median()

    this_df = pd.concat([mean_3day, mean_10day, mean_30day, mean_60day, mean_90day, mean_120day,
                        median_3day, median_10day, median_30day, median_60day, median_90day,
                        median_120day], axis=1) 

    this_df['player'] = player
    this_df['date_game'] = mean_3day.index
    this_df.set_index(['player', 'date_game'], drop=False, inplace=True)
    this_df.columns = [all_rolling] # Must match original rolling_df

    rolling_df = pd.concat([rolling_df, this_df])
    count += 1


# In[37]:


rolling_df.to_csv('./rolling_df.csv')

