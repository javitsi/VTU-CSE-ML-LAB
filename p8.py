import matplotlib.pyplot as plt #output as graph
from sklearn import datasets #from sklearn website import datasets
from sklearn.cluster import KMeans #do the clustering automatically
import pandas as pd
import numpy as np
from sklearn import preprocessing #for mapping the data into particular range
from sklearn.mixture import GaussianMixture 
iris=datasets.load_iris()
X=pd.DataFrame(iris.data) 
X.columns=['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width']
X_norm=preprocessing.normalize(X)
y=pd.DataFrame(iris.target)
y.columns=['Targets']
model=KMeans(n_clusters=3)
model.fit(X_norm)
gmm=GaussianMixture(n_components=3)
gmm.fit(X_norm)
gmm_y=gmm.predict(X_norm)
plt.figure(figsize=(20,20))
colormap=np.array(['red','lime','black'])
plt.subplot(2,2,1)
plt.scatter(X.Petal_Length,X.Petal_Width,c=colormap[model.labels_],s=300)
plt.title('K-Mean Clustering')
plt.xlabel('Petal Length')
plt.ylabel('Petal width')
plt.subplot(2,2,2)
plt.scatter(X.Petal_Length,X.Petal_Width,c=colormap[gmm_y],s=300)
plt.title('gMM Clustering')
plt.xlabel('Petal Length')
plt.ylabel('Petal width')
plt.show()
