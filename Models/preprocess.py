# This file is for copying to a codeblock in notebook to preprocess dev and test data
# Require library
import pandas as pd
import string
import emoji_vietnamese
def preprocess_data(data):
    data['text'] = data['text'].str.replace(
        r'http\S+', '', regex=True).replace(r'www\S+', '', regex=True)
    data['text'] = data['text'].str.replace(
        '['+string.punctuation+']', '', regex=True)
    data['text'] = data['text'].str.lower()
    data['text'] = data['text'].apply(emoji_vietnamese.demojize)
    return data