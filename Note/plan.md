# Problem description
- Bài toán: phân loại câu văn là toxic hay không toxic
- Input: câu văn
- Output: toxic hay không toxic
# Dataset
## [ViCTSD](https://github.com/tarudesu/ViCTSD)
### Description 
- 10000 examples
- 5 trường: Comment, Constructiveness, Toxicity, Title, Topic
    + Comment: câu văn
    + Constructiveness: 0 (non-constructive), 1 (constructive)
    + Toxicity: 0 (non-toxic), 1 (toxic)
    + Title: tiêu đề bài viết
    + Topic: chủ đề bài viết
### Distribution
## [ViHSD](https://github.com/sonlam1102/vihsd)
### Description
- 33400 examples
- 2 trường: Comment, Label
    + Comment: câu văn
    + Label: 0 (clean), 1 (offensive), 2 (hate)
### Distribution    
# Pipeline
## Data explore
- Data distribution
    + Số lượng câu văn toxic và không toxic
    + Số lượng câu văn theo chủ đề
    + Độ dài câu văn
    + Tần suất xuất hiện của từng từ
    + Named entity recognition
- Data visualization
    + Word cloud
    + Histogram
    + Pie chart
    + Heatmap
## Preprocessing
- Data cleaning
- Data augmentation
- Data balancing
- Data splitting
- Tokenization
- Data encoding
    + One-hot encoding
    + Label encoding
    + Byte-level byte pair encoding
    + Word embedding
    + Sentence embedding
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
- Phân tích các case sai để cải thiện model
- Thay đổi các option trong bước preprocessing
- Thay đổi model
## Deployment
- Dùng Flask để tạo API
- Dùng Streamlit để tạo web app demo nhanh