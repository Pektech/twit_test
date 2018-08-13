from app import db
from .models import User, Tweets
import csv
import datetime

#helper functions

def csv_names(csv_file):
    with open(csv_file) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            user = User()
            user.screen_name = row['screen_name']
            db.session.add(user)
            db.session.commit()




def csv_tweets(csv_file):
    with open(csv_file) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            tweet = Tweets()
            tweet.user_id = row['user_id']
            tweet.twt_text = row['twt_text']
            tweet.twt_date = datetime.datetime.strptime(row['twt_date'], '%m/%d/%Y')
            tweet.twt_hash = row['twt_hash']
            db.session.add(tweet)
            db.session.commit()
