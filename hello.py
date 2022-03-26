import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
# from nltk import word_tokenize
# from nltk.probability import FreqDist
# nltk.download('punkt')

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def display():
    return render_template('form.html')


def sentiment_analyzer(string):
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(string)['compound']
    if scores >= 0.5:
        return 'Positive'
    elif scores < 0.5 & scores != 0:
        return 'Negative'
    else:
        return 'Not classified'

# def frequency_words(string):
#     frequency = []
#     words = word_tokenize(string)
#     fdist = FreqDist(words)
#     frequency.append(fdist)
#     return fdist


def subjectivity(string):
    blob = TextBlob(string)
    sub = blob.sentiment[1]
    if sub >= 0.5:
        return 'Subjective'
    else:
        return 'Objective'


@app.route("/post", methods=['GET', 'POST'])
def input_string():
    string = request.form['string']
    if string:
        services = request.form['services']
        if services:
            res_dict = {}
            if 'sentiment' in services:
                res_dict['sentiment'] = sentiment_analyzer(string)
            if 'subjectivity' in services:
                res_dict['subjectivity'] = subjectivity(string)

            return services


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
