import string
import emoji_vietnamese  # type: ignore

def preprocess_data(
    data,
    url=True,
    punctuation=True,
    lowercase=True,
    stopword=False,
    emoji=False
    ):
    # Load stopwords
    with open('./preprocess/Stopwords/vietnamese-stopwords.txt', 'r') as f:
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
