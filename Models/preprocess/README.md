# Import
import sys
sys.path.append('Models')
from preprocess.preprocess import preprocess_data
# Preprocess data
train = preprocess_data(train, url = True, lowercase = True ,punctuation = True, stopword = True, emoji = False)