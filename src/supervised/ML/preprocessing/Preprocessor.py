import pandas as pd
import numpy as np
import seaborn as sns

import re
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from sklearn.feature_extraction.text import TfidfTransformer
from keras.preprocessing.text import text_to_word_sequence
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

'''
This module includes cleaning and vectorising methods, can be applied to process training and testing data
along with vectorising new instances from the user
'''


# Basic cleaning
def clean(data):
    # remove "(<.*?>)" markup
    data = data.apply(lambda x: re.sub('(<.*?>)', ' ', x))
    # remove punctuation marks 
    data = data.apply(lambda x: re.sub('[,\.!?:()"]', '', x))
    # remove whitespace
    data = data.apply(lambda x: x.strip())
    # remove all strings that contain a non-letter
    data = data.apply(lambda x: re.sub('[^a-zA-Z"]',' ',x))
    # convert to lower
    data = data.apply(lambda x: x.lower())

    # tokenisation
    words = data.apply(lambda x: text_to_word_sequence(x)) 

    # remove stop words
    stop_words = set(stopwords.words('english'))
    filtered = words.apply(lambda x: [w for w in x if not w in stop_words])
    data = filtered.apply(lambda x: " ".join(x))

    # lemmatisation
    lemmatizer = WordNetLemmatizer()
    data = data.apply(lambda x: lemmatizer.lemmatize(x))

    return data
    

# Vectorisation    
def tfidf_process(data):
    vec = TfidfTransformer()
    vec = vec.fit(data)
        
    return vec


def bigram(data):
    vec = CountVectorizer(ngram_range=(1, 2))
    vec = vec.fit(data)
        
    return vec

vec = []
def train_test_vectorizer(train, test):
    global vec
    '''
    Receive cleaned datasets and
    returns vectorised training and test partitions
    '''
    bigram_vec = bigram(train)
    vec.append(bigram_vec)
    train_bi = bigram_vec.transform(train)
    test_bi = bigram_vec.transform(test)
        
    tfidf_vec = tfidf_process(train_bi)
    vec.append(tfidf_vec)
    train_tf = tfidf_vec.transform(train_bi)
    test_tf = tfidf_vec.transform(test_bi)
        
    return train_tf, test_tf

def get_vectorizer():
    return vec


def vectorize_new(sentence):
    '''
    Vectorise a new predicting instance
    '''
    global vec 
    review = pd.Series(sentence)
    review = clean(review)

    review_bi = vec[0].transform(review)
    review_tf = vec[1].transform(review_bi)

    return review_tf

    
def file_read_vectorizer(train_dataset, test_dataset):
    '''
    Used to read TrainingSet and TestSet datasets, then apply vectorisation method
    Returns: Vectorised, splitted dataset
    '''
    colnames = ['No.', 'Text', 'Label']
    train = pd.read_csv(train_dataset, names=colnames)
    test = pd.read_csv(test_dataset, names=colnames)
    train = train[1:]
    test = test[1:]
        
    X_train, X_test = train_test_vectorizer(train['Text'], test['Text'])
    y_train, y_test = train['Label'], test['Label']
        
    return X_train, y_train, X_test, y_test
