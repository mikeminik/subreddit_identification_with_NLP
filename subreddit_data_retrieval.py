import praw
import pandas as pd
import datetime

reddit = praw.Reddit(
    client_id='V1HfcNB5ea0meMmhbOqe5A',
    client_secret='gbREmHM3-qwDNEbN5t5s-YuI6q-JEA',
    user_agent='py_dsi_praw',
    username='py_dsi',
    password='dsir-0911'
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
        subreddit_1_data.append([label, post.id, post.created_utc, post.title, post.selftext, post.subreddit, post.upvote_ratio])

futurology = pd.DataFrame(subreddit_1_data, columns = ['type', 'id','created_utc', 'title', 'self_text', 'subreddit', 'upvote_ratio'])
futurology['datetime'] = futurology['created_utc'].apply(lambda time: datetime.datetime.fromtimestamp(time))
futurology.drop('created_utc', axis = 1, inplace = True)
futurology_uniques = futurology.drop_duplicates(subset='id')
futurology_uniques.set_index('id', inplace = True)

futurology_uniques.to_csv('../datasets/futurology_' + str(datetime.date.today())+ '.csv', index=True)

## Scifi

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
        subreddit_2_data.append([label, post.id, post.created_utc, post.title, post.selftext, post.subreddit, post.upvote_ratio])

scifi = pd.DataFrame(subreddit_2_data, columns = ['type', 'id','created_utc', 'title', 'self_text', 'subreddit', 'upvote_ratio'])
scifi['datetime'] = scifi['created_utc'].apply(lambda time: datetime.datetime.fromtimestamp(time))
scifi.drop('created_utc', axis = 1, inplace = True)
scifi_uniques = scifi.drop_duplicates(subset='id')
scifi_uniques.set_index('id', inplace = True)

scifi_uniques.to_csv('../datasets/scifi_' + str(datetime.date.today())+ '.csv', index=True)