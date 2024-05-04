# This file is for copying to a codeblock in notebook to preprocess dev and test data
# Require library
import pandas as pd
import string
import emoji_vietnamese
# For vihsd dataset
def preprocess_data(data):
    data['free_text'] = data['free_text'].str.replace(
        r'http\S+', '', regex=True).replace(r'www\S+', '', regex=True)
    data['free_text'] = data['free_text'].str.replace(
        '['+string.punctuation+']', '', regex=True)
    data['free_text'] = data['free_text'].str.lower()
    data['free_text'] = data['free_text'].apply(emoji_vietnamese.demojize)
    return data
# For victsd dataset
def preprocess_data(data):
    data['Comment'] = data['Comment'].str.replace(
        r'http\S+', '', regex=True).replace(r'www\S+', '', regex=True)
    data['Comment'] = data['Comment'].str.replace(
        '['+string.punctuation+']', '', regex=True)
    data['Comment'] = data['Comment'].str.lower()
    data['Comment'] = data['Comment'].apply(emoji_vietnamese.demojize)
    return data
