import pandas as pd  # type: ignore
import string
import emoji_vietnamese  # type: ignore


def load_data(dataset='vihsd'):
    if dataset == 'vihsd':
        train = pd.read_csv('../Dataset_Reformat/train_vihsd.csv')
        dev = pd.read_csv('../Dataset_Reformat/dev_vihsd.csv')
        test = pd.read_csv('../Dataset_Reformat/test_vihsd.csv')
    elif dataset == 'victsd':
        train = pd.read_csv('../Dataset_Reformat/train_victsd.csv')
        dev = pd.read_csv('../Dataset_Reformat/dev_victsd.csv')
        test = pd.read_csv('../Dataset_Reformat/test_victsd.csv')
    elif dataset == 'merged':
        train = pd.read_csv('../Dataset_Reformat/train_merged.csv')
        dev = pd.read_csv('../Dataset_Reformat/dev_merged.csv')
        test = pd.read_csv('../Dataset_Reformat/test_merged.csv')
    return train, dev, test

def load_data(set_name, dataset='vihsd'):
    valid_sets = ['train', 'dev', 'test']
    if set_name not in valid_sets:
        raise ValueError(f"Invalid set_name. Expected one of: {valid_sets}")

    if dataset == 'vihsd':
        data = pd.read_csv(f'../Dataset_Reformat/{set_name}_vihsd.csv')
    elif dataset == 'victsd':
        data = pd.read_csv(f'../Dataset_Reformat/{set_name}_victsd.csv')
    elif dataset == 'merged':
        data = pd.read_csv(f'../Dataset_Reformat/{set_name}_merged.csv')

    return data


def preprocess_data(
    data,
    url=True,
    punctuation=True,
    lowercase=True,
    stopword=False,
    emoji=False
):
    # Load stopwords
    with open('./utility/Stopwords/vietnamese-stopwords.txt', 'r', encoding='utf-8') as f:
        stopwords = f.read().splitlines()
    # Function to remove stopwords

    def remove_stopwords(text):
        words = text.split()
        words = [word for word in words if word not in stopwords]
        return ' '.join(words)
    if url:
        # Remove URLs
        data['text'] = data['text'].str.replace(
            r'http\S+', '', regex=True).replace(r'www\S+', '', regex=True)
    if punctuation:
        # Remove punctuation
        data['text'] = data['text'].str.replace(
            '['+string.punctuation+']', '', regex=True)
    if lowercase:
        # Lowercase
        data['text'] = data['text'].str.lower()
    if stopword:
        # Remove stopword
        data['text'] = data['text'].apply(remove_stopwords)
    if emoji:
        # Remove emojis
        data['text'] = data['text'].apply(emoji_vietnamese.demojize)
    return data
