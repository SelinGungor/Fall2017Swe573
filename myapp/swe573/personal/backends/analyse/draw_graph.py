import matplotlib.pyplot as plt
import personal.backends.analyse.sentiment_analysis as s
from swe573 import settings

class DrawGraph(object):
    def __init__(self, tweets):
        self.tweets = tweets

    def analyse(self):
        self.number_of_tweets = []
        self.emotions = {}
        self.number_of_tweets_counter = 0
        counter = 1
        for tweet in self.tweets:
            emotion, confidence = s.sentiment(tweet)
            print(tweet + " - " + str(emotion) + " - "+ str(confidence))
            if emotion in self.emotions:
                self.emotions[emotion] += 1
            else:
                self.emotions[emotion] = 1
            self.number_of_tweets_counter += 1
            self.number_of_tweets.append(str(self.number_of_tweets_counter))
        return self.emotions, confidence

    def showGraph(self, emos):
        print(emos)
        fig = plt.figure()
        plt.title('DeepYou - Twitter Sentimental Profiling')
        plt.xlabel('Emotions')
        plt.ylabel('Number of Tweets')
        plt.bar(range(len(emos)), emos.values(), align='center',color='r')
        plt.xticks(range(len(emos)), emos.keys())
        fig.savefig(settings.BASE_DIR + settings.STATIC_URL + '/deepyou.png')  # Use fig. here
        #plt.show(block=True)

# my_tweets = ["I am so bored","I am worried about you","I hope I can wake up early tomorrow","I feel so good. Let's party!","I am so bored","I am worried about you","I hope I can wake up early tomorrow","I feel so good. Let's party!","I am so bored","I am so bored","I am so bored","I am so bored","I am so bored"]
# graph = DrawGraph(my_tweets)
# graph.showGraph()