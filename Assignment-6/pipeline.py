#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 05:13:42 2018

@author: nikhilkamath
"""

import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier 
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import SelectKBest, chi2
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer




def extractTrain():
    data = pd.read_csv('train.txt', sep='\t', header=None)
    np_train = data.values

    train_x=np_train[:, 0]
    train_y=np_train[:, 1]
    return train_x,train_y
    
def extractTest():
    data = pd.read_csv('test-gold.txt', sep='\t', header=None)
    np_test = data.values
    
    test_x=np_test[:, 0]
    test_y=np_test[:, 1]
    return test_x,test_y


def initPipeline(pipelineDict):
    
    # http://dataaspirant.com/2017/05/15/implement-multinomial-logistic-regression-python/
    pipeLogisticReg = Pipeline([
            ('vectorizer', CountVectorizer()),
            ('selection', SelectKBest(chi2)),
            ('log_reg', LogisticRegression(multi_class = 'multinomial', solver = 'newton-cg'))
            ])
    
    
    pipelineDict['Logisticregression'] = pipeLogisticReg
    pipeDecisionTree = Pipeline([
            ('vectorizer', CountVectorizer()),
            ('selection', SelectKBest(chi2)),
            ('decision_tree', DecisionTreeClassifier())
            ])
    
    
    pipelineDict['DecisionTree'] = pipeDecisionTree



    #http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html
    pipeNaiveBayes = Pipeline([
            ('vectorizer', CountVectorizer()),
            ('selection', SelectKBest(chi2)),
            ('naive_bayes', MultinomialNB())
            ])
   
    pipelineDict ['NaiveBayes'] = pipeNaiveBayes



    pipeLinearSVC = Pipeline([
            ('vectorizer', CountVectorizer()),
            ('selection', SelectKBest(chi2)),
            ('linear_svc', LinearSVC(multi_class = 'ovr'))
            ])
    pipelineDict['LinearSVC']= pipeLinearSVC
    
    
    
    
    return pipelineDict

    
def loadModel(train_x, train_y, test_x,test_y, method_name, pipeline):
    
    parameter_grid = {'selection__k': [200]}

    grid_search = GridSearchCV(pipeline, param_grid = parameter_grid, refit = True)
    
    
    predict_train = grid_search.fit(train_x, train_y).predict(train_x)
    
    print('=========================================')
    
    predict_test = grid_search.predict(test_x)
    
    print('Confusion matrix of ' + method_name)
    
    
    print(confusion_matrix(train_y, predict_train))
    
    ax= plt.subplot()
    sns.heatmap(confusion_matrix(test_y, predict_test), annot=True, ax = ax, fmt = 'g')
    
    print('Accuracy score for ' + method_name + ' (Train V test)')
    
    print(str(accuracy_score(train_y, predict_train)) +' '+ str(accuracy_score(test_y, predict_test)))
    print('=========================================')


train_x,train_y = extractTrain()
test_x,test_y = extractTest()
pipelineDict = {}
pipelineDict = initPipeline(pipelineDict)
for item, val in pipelineDict.items():    
    loadModel(train_x,train_y,test_x,test_y,item,val)
