`Preprocessor.py`: Includes cleaning and vectorising methods, can be applied to process training and testing data, along with vectorising new instances from the user


The module includes the following methods:
- `clean`: returns data after basic cleaning techniques (removing stop words, whitespaces, lemmitisation, etc.).
	
- `tfidf_process`: returns the vectoriser that transforms data into vectors by applying Tfidf.
- `bigram`: returns the bigram vectorisor.
	
- `train_test_vectorizer`: receive the clean data training + testing datset, then returns the vectorised partitions (by applying `bigram` and `tfidf_process`)
	
- `file_read_vectorizer`: Read Train and Test datasets, apply `train_test_vectorizer` to vectorize these partiitons. The method returns X_train, y_train, X_test, y_test that can be fed to the model.
	
- `vectorize_new`: receives a review (string) and vectorise it with the same vectoriser applied for the training and testing datasets. This method returns the vectorised review.
	
- `get_vectorizer`: return the vectorizer for training and testing dataset.

You might use this module as follows:
- Retrieve X_train, y_train, X_test, y_test from the method `file_read_vectorizer(train_path, test_path)`
- Use `vectorize_new(sentence)` method to turn the new value into a valid vector. Then predict with the current model as usual.