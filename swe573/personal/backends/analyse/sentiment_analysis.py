import random
import pickle
from nltk.classify import ClassifierI
import swe573.settings as stg
from nltk.tokenize import word_tokenize
import statistics
import os

class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return self.get_mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(self.get_mode(votes))
        conf = choice_votes / len(votes)
        return conf

    def get_mode(self, votes):
        try:
            print("Th¡e Mode = ", statistics.mode(votes))
            mode = statistics.mode(votes)
        except statistics.StatisticsError as e:
            print("There was an error with the statistics module")
            print(e)
            mode = max(set(votes), key=votes.count)
        return mode


url = os.path.join(stg.STATICFILES_DIRS[0], 'pickled_algos_emotions/documents.pickle')
documents_f = open(url, "rb")
documents = pickle.load(documents_f)
documents_f.close()


url = os.path.join(stg.STATICFILES_DIRS[0], 'pickled_algos_emotions/word_features5k.pickle')
word_features5k_f = open(url, "rb")
word_features = pickle.load(word_features5k_f)
word_features5k_f.close()


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

url = os.path.join(stg.STATICFILES_DIRS[0], 'pickled_algos_emotions/featuresets.pickle')
featuresets_f = open(url, "rb")
featuresets = pickle.load(featuresets_f)
featuresets_f.close()

random.shuffle(featuresets)
print(len(featuresets))

testing_set = featuresets[5000:]
training_set = featuresets[:5000]


url = os.path.join(stg.STATICFILES_DIRS[0], 'pickled_algos_emotions/originalnaivebayes5k.pickle')
open_file = open(url, "rb")
classifier = pickle.load(open_file)
open_file.close()

url = os.path.join(stg.STATICFILES_DIRS[0], 'pickled_algos_emotions/MNB_classifier5k.pickle')
open_file = open(url, "rb")
MNB_classifier = pickle.load(open_file)
open_file.close()


url = os.path.join(stg.STATICFILES_DIRS[0], 'pickled_algos_emotions/BernoulliNB_classifier5k.pickle')
open_file = open(url, "rb")
BernoulliNB_classifier = pickle.load(open_file)
open_file.close()

url = os.path.join(stg.STATICFILES_DIRS[0], 'pickled_algos_emotions/LogisticRegression_classifier5k.pickle')
open_file = open(url, "rb")
LogisticRegression_classifier = pickle.load(open_file)
open_file.close()

url = os.path.join(stg.STATICFILES_DIRS[0], 'pickled_algos_emotions/LinearSVC_classifier5k.pickle')
open_file = open(url, "rb")
LinearSVC_classifier = pickle.load(open_file)
open_file.close()


url = os.path.join(stg.STATICFILES_DIRS[0], 'pickled_algos_emotions/SGDC_classifier5k.pickle')
open_file = open(url, "rb")
SGDC_classifier = pickle.load(open_file)
open_file.close()




voted_classifier = VoteClassifier(
                                  classifier,
                                  LinearSVC_classifier,
                                  MNB_classifier,
                                  BernoulliNB_classifier,
                                  LogisticRegression_classifier)




def sentiment(text):
    feats = find_features(text)
    return voted_classifier.classify(feats),voted_classifier.confidence(feats)