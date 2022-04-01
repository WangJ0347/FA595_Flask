# FA595_Flask

# 1 Sentiment analyzer
This service is based on nltk Vader functions. VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool, it is used to quantify how much of positive or negative emotion the text has and also the intensity of emotion.
The servise generates the sentiment analysis of the string provided. On detail, it returns the conpound, the most important mesurement generated from the analysis.
Higher the compound, more positive is the string submitted. In addition the function set a threasold at compound equal to 0.5, if it is higher it states
that the string has a positive sentiment, if it is lower it suggests a negative sentiment.

# 2 Word frequency
This service is based on nltk functions. It generates as response the frequency of each word of the string provided.
It is based on the frequency distribution probability in the nltk package. It returns a list with the frequency of the words.

# 3 Subjectivity
This service is based on TextBlob sentiment analysis. It provides the perceived feeling from the input string in terms of objective or subjective statement. If the result obtained is higher than 0.5 the string most likely is a subjective consideration while it is lower it is an objective speach.

# 4 Part of Speech
This service is based nltk and it uses the word tokenization. It provide the part of the speech for each word. Below the datailed documentation for the most common POS.

IN    preposition/subordinating conjunction 

JJ    adjective 

JJR   adjective, comparative  

JJS   adjective, superlative  

NN    noun, singular 

NNS   noun plural

NNP   proper noun, singular 

POS   possessive ending parent’s 

PRP   personal pronoun

PRP$  possessive pronoun

RB    adverb – very, silently,  

RP    particle – give up 

TO    infinite verb

VB    verb, base form 

VBD   verb, past tense 

VBG   verb, gerund/present participle

VBN   verb, past participle

VBP   verb, sing. present, non-3d 

VBZ   verb, 3rd person sing. present

# 5 From plural to singular and viceversa
This service is based on TextBlob and Part Of Speech nltk. It takes all the noun from a string and if they are singular (NN) the function provide the plural while if it is plural (NNS), it provides the singular. The results are organized in a dictionary.

# 6 Word definitions 
