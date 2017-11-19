import matplotlib.pyplot as plt
import personal.backends.analyse.sentiment_analysis as s

class DrawGraph(object):
    def __init__(self, tweets):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
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

    def showGraph(self, emotions):
        self.emotions = self.analyse()
        print(self.emotions)
        plt.title('DeepYou - Twitter Sentimental Profiling')
        plt.xlabel('Emotions')
        plt.ylabel('Number of Tweets')
        plt.bar(range(len(self.emotions)), self.emotions.values(), align='center',color='r')
        plt.xticks(range(len(self.emotions)), self.emotions.keys())
        plt.show()

# my_tweets = ["I am so bored","I am worried about you","I hope I can wake up early tomorrow","I feel so good. Let's party!","I am so bored","I am worried about you","I hope I can wake up early tomorrow","I feel so good. Let's party!","I am so bored","I am so bored","I am so bored","I am so bored","I am so bored"]
# graph = DrawGraph(my_tweets)
# graph.showGraph()