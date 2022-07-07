# Pretrained Word2Vec x Mini-batch KMeans 

| ![Architecture](https://github.com/tuanlda78202/SAIMDB/blob/main/materials/img/w2v_mbkm.png) | 
|:--:| 
| Word2Vec visualization|


Word2vec algorithms include skip-gram and CBOW models, using either hierarchical softmax or negative sampling
- [Tomas Mikolov et al: Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf)
- [Tomas Mikolov et al: Distributed Representations of Words and Phrases and their Compositionality](https://arxiv.org/abs/1310.4546)

## Cluster Documents  
1. **Cleaning and tokenizing data**: this usually involves lowercasing text, removing non-alphanumeric characters, or stemming words.


2. **Generating vector representations of the documents**: this concerns the mapping of documents from words into numerical vectors—some common ways of doing this include using bag-of-words models or word embeddings. 
    In this repository we used pre-trained `fasttext-wiki-news-subwords-300` mix IMDb data to generate word embeddings.


3. **Applying a clustering algorithm on the document vectors**: this requires selecting and applying a clustering algorithm to find the best possible groups using the document vectors. Some frequently used algorithms include K-means, DBSCAN or Hierarchical Clustering.
