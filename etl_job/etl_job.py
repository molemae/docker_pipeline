# %%
from pymongo import MongoClient
import time
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# %%
#def extract_mongo(conn,client=MongoClient(conn),table):
# Extract: connect to mongodb and get data
conn = 'mongodb://mongo_social'
client = MongoClient(host=conn, port=27017)#'mongodb://localhost:27017'))
db = client.social_DB
time.sleep(5)
print('hey, im connected to the social DB')
toots = list(db.mastodon_table.find())



# %%

# transform: VADER

# %%
# postgres_container:5432
uri = 'postgresql://postgres:postres_pw@postgres_container:5432/social_sentimentDB'
pg = create_engine(uri, echo=True)
print('Im connected to the postgres')
time.sleep(20)
# %% write data and Sentiment Scores to database
for toot in toots:
    df = pd.DataFrame(toot,index=['index'])
    # Sentiment Analysis
    sentiment = SentimentIntensityAnalyzer().polarity_scores(toot['content']) 
    score = sentiment['compound']
    df['score']=[score]
    # print(df)
    # SQL query
    df.to_sql('mastodon',pg, if_exists='append')

print('done with uploading the toots to the postgres') 
# %%
