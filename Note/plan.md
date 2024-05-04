# Problem description
- Problem: Classify whether a sentence is toxic or non-toxic
- Input: Sentence
- Output: Toxic or non-toxic
# Dataset
## [ViCTSD](https://github.com/tarudesu/ViCTSD)
### Description 
- 10000 examples
- 5 columns: Comment, Constructiveness, Toxicity, Title, Topic
    + Constructiveness: 0 (non-constructive), 1 (constructive)
    + Toxicity: 0 (non-toxic), 1 (toxic)
### Distribution
## [ViHSD](https://github.com/sonlam1102/vihsd)
### Description
- 33400 examples
- 2 columns: Comment, Label
    + Label: 0 (clean), 1 (offensive), 2 (hate)
### Distribution    
# Pipeline
## Data explore
- Data distribution
    + Number of toxic and non-toxic sentences
    + Sentence length
- Data visualization
    + Word cloud
    + Histogram
    + Pie chart
## Preprocessing
- Data cleaning
    + Remove nulls, duplicates, #ERROR
    + Lower casing
    + Removal of URLs
    + Removal of Punctuations
    + Removal of Stopwords
    + Conversion of emojis to words
- Data augmentation (Experimental)
- Tokenization: underthesea, vncorenlp, pyvi
- Data encoding
    + One-hot encoding (not recommended)
    + Count vectorization
    + TF-IDF
    + Word embedding (Word2Vec, FastText, GloVe)
    + Byte-level byte pair encoding 
    + Sentence embedding (Doc2Vec, BERT)
## Model
- Machine learning
    + Logistic regression
    + Naive Bayes
    + SVM
    + Random Forest
    + XGBoost
- Deep learning
    + LSTM
    + GRU
    + BiLSTM
    + BiGRU
    + CNN
    + Transformer
    + Bert
## Evaluation & Refinement
- Metrics: Accuracy, F1 score
- Analyze incorrect cases to improve the model
- Change options in the preprocessing step
- Change the model
## Deployment
- Use Flask to create an API
- Use Streamlit to quickly create a web app demo
# Guideline
- Use separate notebooks for each step
- For each model, create 3 version testing on vihsd, victsd, and merged dataset
- Use the same preprocessing steps for all models
- Use the same evaluation metrics for all models