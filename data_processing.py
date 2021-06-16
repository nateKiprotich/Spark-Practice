import requests
from pyspark.sql import SparkSession
import json


spark = SparkSession.builder.getOrCreate()


base_url = 'https://hacker-news.firebaseio.com/v0/'

top_stories_url = base_url + 'topstories.json'
item_url = base_url + 'item/'
new_stories_url = base_url + 'newstories.json'
ask_stories_url = base_url + 'askstories.json'
show_stories_url = base_url + 'showstories.json'
updates_url = base_url + 'updates.json'


response = requests.get(base_url)
top_resp = requests.get(top_stories_url)
new_resp = requests.get(new_stories_url)
ask_resp = requests.get(ask_stories_url)
show_resp = requests.get(show_stories_url)
updates_resp = requests.get(updates_url)


print('Response : ' + str(response.status_code))
print('Top Response : ' + str(top_resp.status_code))
print('New stories response : ' + str(new_resp.status_code))
print('Ask Stories respomse : ' + str(ask_resp.status_code))
print('Show Stories response : ' + str(show_resp.status_code))
print('Updates Response : ' + str(updates_resp.status_code))


if response.status_code == 200:
    print('Connection Established')


print(top_resp.json())
