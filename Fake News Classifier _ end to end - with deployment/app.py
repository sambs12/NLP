# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 16:50:02 2021

@author: sambi
"""

from flask import Flask,render_template,url_for,request
import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
#from sklearn.externals import joblib
import pickle
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,LSTM,Embedding
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re
import nltk



# Load your trained model
app = Flask(__name__)

MODEL_PATH ='model_fake_news.h5'
model = load_model(MODEL_PATH)

from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    
    if request.method == 'POST':
        max_features = 5000
        embed_dimension = 128
        x = ["title"]
        tokenizer = Tokenizer(num_words = max_features, split = ' ')
        from nltk import word_tokenize
        nltk.download('punkt')
        tokenizer.fit_on_texts(x)
        filtered_x = []
        for word in x:
          if word not in stop_words:
            filtered_x.append(word)
        seq1 = tokenizer.texts_to_sequences(filtered_x)
        seq1 = pad_sequences(seq1, maxlen = 22)
        y_pred = model.predict_classes(seq1)
        print(y_pred)
        
    return render_template('result.html',prediction = y_pred)




if __name__ == '__main__':
	app.run(debug=True)