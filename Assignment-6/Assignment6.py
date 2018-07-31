# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
from sklearn.decomposition import TruncatedSVD
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer

def extractTrainTest(train_x):
    
    train_x = train_x.reshape(int(train_x.shape[0]/2),2)
    X = train_x[:, 0]
    Y = train_x[:, 1]
    return X,Y

def countVectorize(X):
    vectorizer = CountVectorizer()
    X_vectorized = vectorizer.fit_transform(X)
    return X_vectorized


def plotPCA(X_vectorized):
    svd = TruncatedSVD(n_components = 14)
    X_svd = svd.fit(X_vectorized).transform(X_vectorized)
    
    
    plot_df = pd.DataFrame({'X1':X_svd[:,0],'X2':X_svd[:,1], 'X3':X_svd[:,2], 'X4':X_svd[:,3],
                       'X5':X_svd[:,4], 'X6':X_svd[:,5], 'X7':X_svd[:,6], 'X8':X_svd[:,7],
                       'X9':X_svd[:,8], 'X10':X_svd[:,9], 'X11':X_svd[:,10], 'X12':X_svd[:,11],
                       'X13':X_svd[:,12], 'X14':X_svd[:,13],
                       'y':y})
    sns.set(style="dark")
    
    sns.pairplot(plot_df, hue = "y")

data = pd.read_csv('train.txt', sep='\t', header=None)


train = data.values


#seperate unique labels
distinct_y = np.unique(train[:, 1])

start= 0
end = 300

train_x = train[1, :]
for label in distinct_y:
    
    data_y = train[train[:, 1] == label]
    for i in range(start, end):
        train_x = np.concatenate((train_x, data_y[i, :]))
        
    start = end
    end = end + 300


X,Y = extractTrainTest(train_x)
xv = countVectorize(X)
plotPCA(xv)



