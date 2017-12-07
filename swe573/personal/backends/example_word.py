#import sentiment_mod as s
#import ..sentiment_mod as s
from sentiment_mod import sentiment, featuresets

print(featuresets[:2])

print(sentiment("This movie was awesome! The acting was great, plot was wonderful"))


print(sentiment("This movie was utter junk! I don't see what the point was at all. Horrible movie, 0/10."))
