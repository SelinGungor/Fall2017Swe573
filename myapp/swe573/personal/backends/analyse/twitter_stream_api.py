import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import MySQLdb
import time
import json
import datetime
import personal.backends.analyse.draw_graph as gr

#consumerkey, consumersecret #https://apps.twitter.com/ #deepyou
csecret = 'VH8mYzkEvPEqGNlZTZnFnq3WS1aO0VpVQWwq1mHNz9T82lUwEw'
ckey = 'AoxuI3HzTsLzjVSdqfFHKMWCo'
atoken = '747662208-qTHmkAmDK5SzV5cN4dh80JkjaRYerUcbQIrdpYqe'
asecret = '8GHntLvtP88Yz7rsflSAz6cUHbSX1imeGQJXC6b1qzlXH'

# #mysql connection
# conn = MySQLdb.connect("selingungor.mysql.pythonanywhere-services.com", "selingungor", "MyDeepYouP@ss", "selingungor$deepyou")
# connection = conn.cursor()


class DeepYou(object):
    def __init__(self, username):
        self.username = username

    def give_analyse_result(self):
        auth = tweepy.OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)

        # twitterStream = tweepy.Stream(auth, listener())
        # my_tweets = twitterStream.filter(track=["a"], languages=["en"])
        emoemo = {}
        api = tweepy.API(auth)
        #get my tweets
        try:
            my_tweet_list = []
            for status in tweepy.Cursor(api.user_timeline, screen_name=self.username).items():
                my_tweets = status._json['text']
                my_tweet_list.append(my_tweets)
                out = open('verizon_twitter_data.txt', 'a+')
                my_tweets = my_tweets.encode('utf-8')
                out.write(str(my_tweets) + "\n")
            result = Result(my_tweet_list)
            my_emotions = result.analyse_emotions()
                #print(my_tweet_list + " - " + my_emotions)
            emoemo[list(my_emotions.keys())[0]] = list(my_emotions.values())
        except KeyError:
            print("key error!!!!!!!!!!")
        print(my_emotions)
        result.show_graph(my_emotions)



class Listener(tweepy.StreamListener):
    def on_data(self, data):
        try:
            all_data = json.loads(data)
            tweet_list = []
            tweet = all_data["text"]
            tweet_list.append(tweet)
            out = open('verizon_twitter_data.txt', 'a+')
            tweet = tweet.encode('utf-8')
            out.write(str(tweet) + "\n")
        except KeyError:
            print("key error!!!!!!!!!!")
        print(tweet_list)
        return tweet_list

    def on_error(self, status):
        print(status)
        return False

class Result(object):
    def __init__(self, tweets):
        self.tweets = tweets
        self.graph = gr.DrawGraph(self.tweets)

    def analyse_emotions(self):
        #graph = gr.DrawGraph(self.tweets)
        emotions, confidence = self.graph.analyse()

        if confidence*100 >= 50:
            output = open("twitter-out.txt","a")#add "a"
            output.write('{}'.format(list(emotions.keys())))
            output.write("\n")
            output.close()

        print(type(emotions))
        print(emotions)
        time.sleep(0.2)
        return emotions

    def show_graph(self, emos):
        #graph = gr.DrawGraph(self.tweets)
        self.graph.showGraph(emos)


#giveAnalyseResult('@erolstt') #if you uncomment this line, analyzing emotions will start when you execute app from terminal, please uncomment it just for testinf purposes


# import matplotlib.pyplot as plt
# def showGraph(emos):
#     print(emos)
#     plt.title('DeepYou - Twitter Sentimental Profiling')
#     plt.xlabel('Emotions')
#     plt.ylabel('Number of Tweets')
#     plt.bar(range(len(emos)), emos.values(), align='center',color='r')
#     plt.xticks(range(len(emos)), emos.keys())
#     plt.show()

##
#
# api = tweepy.API(auth)
#
# username = sys.argv[1]
# startDate = datetime.datetime(2014, 6, 1, 0, 0, 0)
# endDate =   datetime.datetime(2015, 1, 1, 0, 0, 0)
#
# tweets = []
# tmpTweets = api.user_timeline(username)
# for tweet in tmpTweets:
#     if tweet.created_at < endDate and tweet.created_at > startDate:
#         tweets.append(tweet)
#
# while (tmpTweets[-1].created_at > startDate):
#     print("Last Tweet @", tmpTweets[-1].created_at, " - fetching some more")
#     tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id)
#     for tweet in tmpTweets:
#         if tweet.created_at < endDate and tweet.created_at > startDate:
#             tweets.append(tweet)