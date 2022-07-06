'''
Puspose: This code was create to find all the relavent user from a specific hashtag
date: 2022.07.06
Author: Khandoker Tanjim Ahammad
Parameter: Main parameter is the hashtag keyword , then the dates and also we can specify the langue too 
Comments:




'''
#import dependencies 
import pandas as pd
import tweepy
import time
# dataframe function for excel file to display data of each tweet
def printtweetdata(n, ith_tweet):
        print()
        print(f"Tweet {n}:")
        print(f"Username:{ith_tweet[0]}")
        print(f"Description:{ith_tweet[1]}")
        print(f"Location:{ith_tweet[2]}")
        print(f"Following Count:{ith_tweet[3]}")
        print(f"Follower Count:{ith_tweet[4]}")
        print(f"Total Tweets:{ith_tweet[5]}")
        print(f"Retweet Count:{ith_tweet[6]}")
        print(f"Tweet Text:{ith_tweet[7]}")
        print(f"Hashtags Used:{ith_tweet[8]}")
 
 
# main data function which will be scrape from twitter to perform data extraction
def scrape(words, date_since, numtweet):
 
        # Creating Dataframe using pandas
        db = pd.DataFrame(columns=['username',
                                   'description',
                                   'location',
                                   'following',
                                   'followers',
                                   'totaltweets',
                                   'retweetcount',
                                   'text',
                                   'hashtags'])
 
        
    

        # we can also add lang="en" for specify the language in 
        #tweepy.Cursor(api.search_tweets,words,lang="en"since_id=date_since,tweet_mode='extended').items(numtweet)
        tweets = tweepy.Cursor(api.search_tweets,
                               words,
                               since_id=date_since,
                               tweet_mode='extended').items(numtweet)
 
        list_tweets = [tweet for tweet in tweets]

        i = 1
 
        for tweet in list_tweets:
                username = tweet.user.screen_name
                description = tweet.user.description
                location = tweet.user.location
                following = tweet.user.friends_count
                followers = tweet.user.followers_count
                totaltweets = tweet.user.statuses_count
                retweetcount = tweet.retweet_count
                hashtags = tweet.entities['hashtags']
 
                try:
                        text = tweet.retweeted_status.full_text
                except AttributeError:
                        text = tweet.full_text
                hashtext = list()
                for j in range(0, len(hashtags)):
                        hashtext.append(hashtags[j]['text'])
 
                # Here we are appending all the
                # extracted information in the DataFrame
                ith_tweet = [username, description,
                             location, following,
                             followers, totaltweets,
                             retweetcount, text, hashtext]
                db.loc[len(db)] = ith_tweet
 
                # Function call to print tweet data on screen
                printtweetdata(i, ith_tweet)
                i = i+1
        #filename = 'match_one_tweets.xlsx'
        filename = str('_hashtag_list_')+str(current_date.year)+str('_')+str(current_date.month)+str('_')+str(current_date.day)
        # we will save our database as a CSV file.
        db.to_excel(words+filename,index=False)
 
if __name__ == '__main__':
 
        # Enter your own credentials obtained
        # from your developer account
        consumer_key = "api key"
        consumer_secret = "api key"
        access_key = "api key"
        access_secret = "api key"
 
 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)
 
        # Enter Hashtag and initial date
        print("Enter Twitter HashTag to search for")
        words = input()
        print("Enter Date since The Tweets are required in yyyy-mm--dd")
        date_since = input()
 
        # number of tweets you want to extract in one run
        numtweet = 1000
        scrape(words, date_since, numtweet)
        print('Scraping has completed!')
