from sklearn.datasets import fetch_20newsgroups 
categories = ['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med']
news_train=fetch_20newsgroups(subset="train",categories=categories,shuffle="True")
news_test=fetch_20newsgroups(subset="test",categories=categories,shuffle="True")
print('Number of Training Examples',len(news_train))
print('Number of Training Examples',len(news_test))
print(news_train.target_names)
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
text_clf = Pipeline([('vect', TfidfVectorizer()), 
                      ('clf', MultinomialNB()) ])

# train the model
text_clf.fit(news_train.data, news_train.target)
# Predict the test cases
predicted = text_clf.predict(news_test.data)

from sklearn import metrics
from sklearn.metrics import accuracy_score
import numpy as np

print('Accuracy achieved is ' + str(np.mean(predicted == news_test.target)))
print(metrics.classification_report(news_test.target, predicted, target_names=news_test.target_names)),
print('confusion Matrix \n',metrics.confusion_matrix(news_test.target, predicted))
