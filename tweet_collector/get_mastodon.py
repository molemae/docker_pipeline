#%%
# import
from mastodon import Mastodon
from pprint import pprint
from pymongo import MongoClient 
from bs4 import BeautifulSoup

#%%
# get latest tweets from mastodon 
m = Mastodon(api_base_url="https://mastodon.social")
toots = m.timeline_hashtag(hashtag='python')

#%%
# go through the full response and save each content with the corresponding id 
mongo_dict = list()
for post in toots:
    id_ = str(post.get('id'))
    name = post.get('account').get('username')
    content = BeautifulSoup(markup=post.get('content'), features='html.parser').get_text()
    if content == '':
        continue
    temp_dict = dict()
    temp_dict['_id'] = id_
    temp_dict['user'] = name
    temp_dict['content'] = content
    mongo_dict.append(temp_dict)

pprint(mongo_dict)

# %%
## Connect to container, create DB and collections in DB
conn = 'mongodb://mongo_social' # or: conn = # 'mongodb://localhost'
client = MongoClient(conn)

#%%
## Create "population_DB"
social_DB = client.social_DB

#%%
## Create and Update "mastodon"
social_DB.mastodon_table.insert_many(mongo_dict)
