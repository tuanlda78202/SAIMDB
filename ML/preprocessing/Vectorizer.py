import pandas as pd

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

        
        
def tfidf_process(data):
    vec = TfidfTransformer()
    vec = vec.fit(data)
        
    return vec
    
    
def bigram(data):
    vec = CountVectorizer(ngram_range=(1, 2))
    vec = vec.fit(data)
        
    return vec
    
    
def dataset_vectorizer(train, test):
    bigram_vec = bigram(train)
    train_bi = bigram_vec.transform(train)
    test_bi = bigram_vec.transform(test)
        
    tfidf_vec = tfidf_process(train_bi)
    train_tf = tfidf_vec.transform(train_bi)
    test_tf = tfidf_vec.transform(test_bi)
        
    return train_tf, test_tf
    
    
def file_read(train_dataset, test_dataset):
    colnames = ['No.', 'Text', 'Label']
    train = pd.read_csv(train_dataset, names=colnames)
    test = pd.read_csv(test_dataset, names=colnames)
    train = train[1:]
    test = test[1:]
        
    X_train, X_test = dataset_vectorizer(train['Text'], test['Text'])
    y_train, y_test = train['Label'], test['Label']
        
    return X_train, y_train, X_test, y_test

def vectorize(sentence):  # vectorize one sentence
    bigram_vec = bigram(sentence)
    sentence_bi = bigram_vec(sentence)

    tfidf_vec = tfidf_process(sentence_bi)
    sentence_tf = tfidf_vec.transform(sentence_bi)

    return sentence_tf