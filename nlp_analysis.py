import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

with open('Reviews/cowboy.txt', 'r') as f:
    text = f.read()
    reviews = nltk.sent_tokenize(text)

analyzer = SentimentIntensityAnalyzer()

compound_avg=0
positive_avg=0
negative_avg=0
neutral_avg=0

for paragraph in reviews:
    print(paragraph)
    ss = analyzer.polarity_scores(paragraph)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    compound_avg += ss['compound']
    positive_avg += ss['pos']
    negative_avg += ss['neg']
    neutral_avg += ss['neu']
    print()

print("total compound score is:  ", compound_avg/len(reviews))
print("total positive score is:  ", positive_avg/len(reviews))
print("total negative_avg score is:  ", negative_avg/len(reviews))
print("total neutral_avg score is:  ", neutral_avg/len(reviews))