# SAIMDB - Sentiment Analysis with IMDb Dataset

| ![Architecture](https://github.com/tuanlda78202/MLP/blob/main/materials/img/mindmap1.png) | 
|:--:| 
| Mindmap SAIMDB Project|

# Abstract
Humans are naturally dependent of the opinions and experience of others, thus have a high tendency to seek the reviews of products before trying out themselves. However, it would be painful to scour the correct information from a multitude of reviews present on the internet.


Sentiment analysis is a powerful method to obtain helpful information about a review and classify it as positive or negative sentiment. In this Sentiment Analysis with IMDb Movie Reviews Project, we wish to apply Machine Learning and Deep Learning approaches to measure the accuracy of the model and identify the best algorithm for sentiment analysis.


IMDb Reviews is a large dataset for binary sentiment classification, consisting of 50,000 highly polar reviews (in English) with an even number of examples for training and testing purposes. The dataset contains additional unlabelled data. A negative review has a score ≤ 4 out of 10, and a positive review has a score ≥ 7 out of 10. No more than 30 reviews are included per movie.


After text processing phase with Word Vectorisation, we will implement multiple algorithms to evaluate the accuracy. ML algorithms are traditional algorithms including Supervised Learning (KNN, Naive Bayes, Decision Tree, Random Forest, SVM, Logistic Regression) and Unsupervised Learning (K-Means Clustering), whereas DL algorithms work with multilayers artificial neural network and are expected to give better output. The output of the model is to classify a movie review as Positive (1) or Negative (0).


You can research more and more with materials in [Machine Learning Research](https://github.com/tuanlda78202/MLR)
# Directories 
- [`materials`](https://github.com/tuanlda78202/SAIMDB/tree/main/materials): All things requirement for project 
  - [`materials/img`](https://github.com/tuanlda78202/SAIMDB/tree/main/materials/img): Mind map `.xmind` and image `.png`
  - [`materials/papers`](https://github.com/tuanlda78202/SAIMDB/tree/main/materials/papers): Top tier paper research need for project.
- [`src`](https://github.com/tuanlda78202/SAIMDB/tree/main/src): Source code, implement by Scikit-learn & Keras TensorFlow
  - [`src/ml`](https://github.com/tuanlda78202/SAIMDB/tree/main/src/ml): Machine Learning Code (TFIDF + SVM)
  - [`src/dl`](https://github.com/tuanlda78202/SAIMDB/tree/main/src/dl): Deep Learning Code (Word Embedding, Word2Vec + Bi-Directional LSTM, BERT)
    - [`src/dl/DBLSTM`](https://github.com/tuanlda78202/SAIMDB/tree/main/src/dl/DBLSTM): Deep Bidirectional LSTM 
    - [`src/dl/UMLFiT`](https://github.com/tuanlda78202/SAIMDB/tree/main/src/dl/UMLFiT):  Universal Language Model Fine-tuning
## Collaborators 
| Name                         | Student ID       | Email                                      |
| :---                         |    :----:        |          :---:                             |
| Le Duc Anh Tuan              | 20204929         | tuan.lda204929@sis.hust.edu.vn            |
| Nguyen Van Thanh Tung             | 20190090         | tung.nvt190090@sis.hust.edu.vn            |
| Hoang Long Vu             | 20204897         | vu.hl204897@sis.hust.edu.vn|
| Nguyen Huu Tuan Duy      | 20204907         | duy.nht204907@sis.hust.edu.vn              |
| Hoang Gia Nguyen          | 20204889         | nguyen.hg204889@sis.hust.edu.vn             |

## Announcements
All older announcements can be found in `ANNOUNCEMENTS.md`

