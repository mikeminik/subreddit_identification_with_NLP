#!/usr/bin/env python
# coding: utf-8

# In[77]:


import praw
import pandas as pd
import datetime

config = pd.read_json('../config.json', typ='series')

reddit = praw.Reddit(
    client_id=config['client_id'],
    client_secret=config['client_secret'],
    user_agent=config['user_agent'],
    username=config['username'],
    password=config['password']
)

## Futurology

subreddit_1 = reddit.subreddit('futurology')

hot_posts = subreddit_1.hot(limit=1000)
rising_posts = subreddit_1.rising(limit=1000)
new_posts = subreddit_1.new(limit=1000)
top_posts = subreddit_1.top(limit=1000)

listings = [(hot_posts, 'hot'), 
            (rising_posts, 'rising'),
            (new_posts, 'new'),
            (top_posts, 'top')
           ]

subreddit_1_data = []
for listing, label in listings:
    for post in listing:
        subreddit_1_data.append([label, post.id, post.created_utc, post.title, post.selftext, post.subreddit, post.upvote_ratio, post.url, post.author])

futurology = pd.DataFrame(subreddit_1_data, columns = ['type', 'id','created_utc', 'title', 'self_text', 'subreddit', 'upvote_ratio', 'link_address', 'user'])

futurology['datetime'] = futurology['created_utc'].apply(lambda time: datetime.datetime.fromtimestamp(time))

futurology.drop('created_utc', axis = 1, inplace = True)

futurology_uniques = futurology.drop_duplicates(subset='id')

futurology_uniques.set_index('id', inplace = True)


futurology_uniques.to_csv('../datasets/futurology_' + str(datetime.date.today())+ '_with_links.csv', index=True)

subreddit_2 = reddit.subreddit('scifi')

hot_posts = subreddit_2.hot(limit=1000)
rising_posts = subreddit_2.rising(limit=1000)
new_posts = subreddit_2.new(limit=1000)
top_posts = subreddit_2.top(limit=1000)

listings = [(hot_posts, 'hot'), 
            (rising_posts, 'rising'),
            (new_posts, 'new'),
            (top_posts, 'top')
           ]

subreddit_2_data = []
for listing, label in listings:
    for post in listing:
        subreddit_2_data.append([label, post.id, post.created_utc, post.title, post.selftext, post.subreddit, post.upvote_ratio, post.url, post.author])

scifi = pd.DataFrame(subreddit_2_data, columns = ['type', 'id','created_utc', 'title', 'self_text', 'subreddit', 'upvote_ratio', 'link_address', 'user'])

scifi['datetime'] = scifi['created_utc'].apply(lambda time: datetime.datetime.fromtimestamp(time))

scifi.drop('created_utc', axis = 1, inplace = True)

scifi_uniques = scifi.drop_duplicates(subset='id')

scifi_uniques.set_index('id', inplace = True)

scifi_uniques.to_csv('../datasets/scifi_' + str(datetime.date.today())+ '_with_links.csv', index=True)

