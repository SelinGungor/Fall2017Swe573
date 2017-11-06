# import tweepy
# from tweepy import OAuthHandler
# from tweepy.streaming import StreamListener
# import MySQLdb
# import time
# import json
# import sentiment_mod as s
# from django.conf import settings as settings
#
# class listener(tweepy.StreamListener):
#     def on_data(self, data):
#         all_data = json.loads(data)
#         tweet = all_data["text"]
#         sentiment_value, confidence = s.sentiment(tweet)
#
#       #  username = all_data["user"]["screen_name"]
#       #  connection.execute("INSERT INTO taula (time, username, tweet) VALUES (%s,%s,%s)",
#       #           (time.time(), username, tweet))
#       # conn.commit()
#
#         #print((username, tweet))
#         print(tweet, sentiment_value, confidence)
#
#         if confidence*100 >= 80:
#             output = open("twitter-out.txt","a")
#             output.write(sentiment_value)
#             output.write("\n")
#             output.close()
#
#         time.sleep(0.2)
#         return True
#
#     def on_error(self, status):
#         print(status)
#
#
# auth = tweepy.OAuthHandler(settings.SOCIAL_AUTH_TWITTER_KEY, settings.SOCIAL_AUTH_TWITTER_SECRET)
# auth.set_access_token(atoken, asecret)
#
# twitterStream = tweepy.Stream(auth, listener())
# twitterStream.filter(track=["today"])