import requests
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType
import json


spark = SparkSession.builder.getOrCreate()


# This function takes in dictionary and prompts user to select a particular story
def select_stories(story_types):
    print('Select story category you want to view')
    
    for key, value in zip(story_types.keys(), story_types.values()):
        print(str(key) + ' ' + value)
    
    selection = int(input('Enter your selection : '))

    selection = story_types.get(selection)

    return selection



'''
show_resp = requests.get(show_stories_url)


for i in show_resp.json():
    it_url = item_url + str(i) +'.json'
    it_resp = requests.get(it_url)
    print(it_resp.json())
'''

if __name__ == "__main__":
    
    base_url = 'https://hacker-news.firebaseio.com/v0/'
    
    end_points = {
                1: "topstories",
                2: "newstories",
                3: "askstories",
                4: "showstories",
                5: "updates"
            }

    selected_end_point = select_stories(end_points)
    selected_end_point_url = base_url + selected_end_point + '.json'

    item_url = base_url + 'item/'

    print('Your will get stories for ' + selected_end_point + ' through url : ' + selected_end_point_url)

    response = requests.get(selected_end_point_url)
    print(response.json())

