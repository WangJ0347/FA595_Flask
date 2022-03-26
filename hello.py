import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
from nltk import word_tokenize
from nltk.probability import FreqDist

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
        return 'positive'
    elif scores < 0.5 & scores != 0:
        return 'negative'
    else:
        return 'not classified'


def frequency_words(string):
    frequency = []
    words = word_tokenize(string)
    fdist = FreqDist(words)
    frequency.append(fdist)
    return frequency[0]


def subjectivity(string):
    blob = TextBlob(string)
    sub = blob.sentiment[1]
    if sub >= 0.5:
        return 'subjective'
    else:
        return 'objective'


def pos(string):
    token = nltk.word_tokenize(string)
    tags = nltk.pos_tag(token)
    return tags


def plural_singular_nouns(string):
    blob = TextBlob(string)
    sentence = blob.sentences[0]
    results = pd.DataFrame(sentence.tags)
    results.columns = ['words', 'pos']
    sing = results[results['pos'] == 'NN']['words'].values
    plur = results[results['pos'] == 'NNS']['words'].values
    if len(sing) != 0 and len(plur) != 0:
        return {"Singular nouns": sing[0],
                "Plural nouns": plur[0]}
    elif len(plur) == 0 and len(sing) != 0:
        return {"singular nouns": sing[0]}
    elif len(sing) == 0 and len(plur) != 0:
        return {"plural nouns": plur[0]}
    else:
        return "no noun founds!"

@app.route("/post", methods=['GET', 'POST'])
def input_string():
    if request.method == 'POST':
        string = request.form['string']
        if string:
            services = request.form.getlist('services')
            if services:
                res_dict = {}
                if 'sentiment' in services:
                    res_dict['Sentiment'] = sentiment_analyzer(string)
                if 'subjectivity' in services:
                    res_dict['Subjectivity'] = subjectivity(string)
                if 'frequency' in services:
                    res_dict['Frequency'] = frequency_words(string)
                if 'pos' in services:
                    res_dict['POS tags'] = pos(string)
                if 'plural_singular' in services:
                    res_dict['Singular & Plural nouns'] = plural_singular_nouns(string)
                return {"success": True, 'response': res_dict}
            else:
                return {'success': False, 'error': 'No listed service submitted'}, 400
        else:
            return {'success': False, 'error': 'No string found'}, 400
    else:
        return render_template('form.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
