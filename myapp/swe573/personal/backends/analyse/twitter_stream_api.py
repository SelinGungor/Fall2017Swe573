import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import MySQLdb
import time
import json
import personal.backends.analyse.draw_graph as gr

#consumerkey, consumersecret #https://apps.twitter.com/ #deepyou
csecret = 'VH8mYzkEvPEqGNlZTZnFnq3WS1aO0VpVQWwq1mHNz9T82lUwEw'
ckey = 'AoxuI3HzTsLzjVSdqfFHKMWCo'
atoken = '747662208-qTHmkAmDK5SzV5cN4dh80JkjaRYerUcbQIrdpYqe'
asecret = '8GHntLvtP88Yz7rsflSAz6cUHbSX1imeGQJXC6b1qzlXH'

# #mysql connection
# conn = MySQLdb.connect("selingungor.mysql.pythonanywhere-services.com", "selingungor", "MyDeepYouP@ss", "selingungor$deepyou")
# connection = conn.cursor()

class listener(tweepy.StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        tweet_list = []
        tweet = all_data["text"]
        print(tweet)
        tweet_list.append(tweet)

        print(tweet_list)
        graph = gr.DrawGraph(tweet_list)
        emotions, confidence = graph.analyse()

        if confidence*100 >= 50:
            output = open("twitter-out.txt","a")#add "a"
            #output.write(emotions.keys())
            output.write('{}'.format(list(emotions.keys())))
            output.write("\n")
            output.close()

        print(emotions)
        graph.showGraph(emotions)
        time.sleep(0.2)
        return True

    def on_error(self, status):
        print(status)

    def deleteContent(self, pfile):
        pfile.seek(0)
        pfile.truncate()


auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = tweepy.Stream(auth, listener())
twitterStream.filter(track=["today"])