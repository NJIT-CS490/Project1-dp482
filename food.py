import tweepy
import flask
import random
import os
import sys
import requests
from os.path import join, dirname
from dotenv import load_dotenv
import json

app = flask.Flask(__name__)

dotenv_path = join(dirname(__file__), 'food.env')
load_dotenv(dotenv_path)

consumer_key= os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token= os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = tweepy.API(auth)

spoonacular_key = os.environ['SPOONACULAR_KEY']

@app.route('/') 
def index():
  
  items=["Pav Bhaji", "Alfredo Pasta", "Nachos", "Jalebi","Quesadilla","Enchilada","Chilli Paneer"]
  select=random.choice(items)
  keyword=auth_api.search(q=select, tweet_mode='extended')
  
  for tw in keyword:
    tweet=(tw.full_text)
    user=(tw.user.screen_name)
    date=(tw.created_at)
    at=(tw.user.location)
    
    return flask.render_template(
      "food.html",
      name = select,
      tweet = tweet,
      user = user,
      time = date,
      location = at,
      )
      
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)