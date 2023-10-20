# Subbreddit Identification Using NLP

The Venture Capital firm "Breakthrough Capital LLC" has contracted us to aid in their mission statement "**Stay ahead of the curve by identifying and investing in the most promising emerging technologies**".

The firm has been late to the party for several emerging technology investment targets and wishes to better engage with significant sources of discussion about futurism and human development technology to more quickly begin the research phase of their portfolio strategy.

Using Natural Language Processing and machine learning, we will help them sort fact from fiction in the face of a high amount of data. Our model will identify posts from the r/Futurology subreddit (fact) and extract popular terms and sources of information, while filtering noise from other subreddits like r/Scifi (fiction). We also want to make sure that topics on Futurology are not misclassified, so we must optimize for Type II errors.

"_Can we identify the the origin of Reddit posts while minimizing Type II errors so topics of interest (investment targets) are not missed?_"

# Data Dictionary

All datasets include Reddit post data and engineered variations of it. Post data has been sourced using PRAW via the Reddit API.

|Feature|Type|Description|
|---|---|---|
|Id|object|  Post unique identifier
|type| object | Sorting method for the post - New, Hot, or Top 
|title| object |  Post title
|self_text| object | If present, accompanying description text on the post 
|subreddit | int64 | Identifies the subreddit either by name, or by 1 = Futurology, 0 = Scifi 
|upvote_ratio | float | Ratio of upvotes  expectancy across sample country population per year
|link_address | object | External URL, if present
|user | object | User ID
|datetime | datetime | Post created UTC
|title_length_chars | int64 | Title length in characters
|title_length_words | int64 | Title length in words
|title_avg_word_length | float | Average word length in title
|url_content | object | Tokenized content of the URL past the domain, if not Reddit
|url_domain | object | Domain of the external link, if not Reddit
|external_link | int64 | bool indicating external link if 1, reddit link if 0

# Instructions for use

If attempting to replicate this project, to make a Reddit connection through PRAW the user must establish a config.json file with format:

```
{
    client_id:"CLIENT_ID"
    client_secret:"CLIENT_SECRET"
    user_agent:"USER_AGENT"
    username:"USERNAME"
    password:"PASSWORD"
}
```
the config.json file must contain credentials that can be obtained by registering a new app through Reddit directly. The file must exist at the top level of the repo by default. 

# Executive Summary

r/Futurology posts were correctly identified in the production model 98% of the time. This resulted in a Recall rate of 96.5% (indicating 3.5% of r/Futurology posts were misclassified as r/Scifi). However, analysis of some false negatives shows that misclassified posts included admin posts unrelated to the topic of either subreddit, such as a ubiquitous call to action to fight the recent Reddit API changes - a topic that was present on many large subreddits. 

The rate of false positives was higher, but it is imagined that sifting these out of research opportunities should require little effort, given the often fanciful nature.

Popular topics of Futurology were extracted from the production data and include such items as:
- Climate change
- Renewable energy
- Facial recognition
- Universal basic income effects
- Self driving cars
- Lab grown protein


Popular news sources were also idenified, including those such as:

- The Guardian
- Business Insider
- Interesting Engineering
- Cnbc
- Electrik
- Reuters
- Bloomberg




# Areas for further research

- This project used "Top" posts to help in NLP subreddit identification but likely adversely affected the extracted data in that it was dated. The model could be re-evaluated without this.
- Training could be done against other subreddits to verify integrity of classification
- The volume of posts could be increased over time

## Citations

**Thank you to the following for their involvement in various aspects of the project:**

- Tim Book for instructional material on Python, Pandas, Matplotlib, Seaborn, and SciKit-Learn, all of which was used here
- Rowan Schaefer for direct assistance with CountVectorizing and Column Transformation
- Google Bard for presentation prompt ideas, and for some confirmations on modeling techniques that were chosen


**Sources on external data:**

Subreddit information via Reddit.com


**Additional thanks to creators and contributors to the following technologies:**

- Python language
- Matplotlib.pyplot library 
- Pandas library
- Numpy library
- Seaborn library
- SciKit-Learn
- Slidesco Presentation Templates

