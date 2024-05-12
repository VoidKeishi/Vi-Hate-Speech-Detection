# Import
import sys
sys.path.append('Models')
from utility.utility import preprocess_data, load_data
# Load data
train, dev, test = load_data('merged')
# Preprocess data
train = preprocess_data(train, url = True, lowercase = True ,punctuation = True, stopword = True, emoji = False)