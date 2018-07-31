# Assignment - 6

**Analyzing data patterns and different classification methods**

**Submitted To**

```
Suhaib Qaiser
```

**Submitted By**

Aman Tewary (B00782684)

Nikhil Kamath (B00779777)

```
Submitted On
July 17, 2018
```

## Table Of Content

- Task Description
- Feature Extraction and Selection
- Classification Algorithm
  - Code to save NB in pipeline [Figure 2]
  - Code to save Logistic Regression in pipeline [Figure 3]
  - Code to save Decision tree in pipeline [Figure 4]
  - Code to save LinearSVC in pipeline [Figure 5]
  - Pairplot [Figure 1]
- Output
  - Confusion Matrix of LinearSVC [Figure 6]
  - Confusion Matrix of Decision Tree [Figure 7]
  - Confusion Matrix of Naive Bayes [Figure 8]
  - Confusion Matrix of Logistic Regression [Figure 9]
- Accuracy Comparison
  - Accuracy of all models Train V Test [Figure 10]
- Reference

## Task Description

The objective of this assignment was to install scikit-learn library for python, retrieve
language dataset from DSL and perform language classification using four different machine
learning algorithm. After training the models, we ran accuracy test for all the models in the
pipeline to showcase which model had the highest accuracy.

## Feature Extraction and Selection

Before extracting the features from the training dataset, we ran PCA to determine which
labels are best fit for classification by performing Kbest method using chi-square. The data
was dense and it doesn’t really work properly with PCA, so we used truncatedSVD to plot
the relation in figure[1]. The plots helps us to understand the label subsequently saving us
the time to train the data by eliciting the relation between each feature with other. The plot
also helps us to visualize the number of labels present in the data viz. 14.

## Classification Algorithm

We were instructed to use four different classification algorithms namely, Naive Bayes,
LinearSVC, Decision Tree and Logistic Regression. We loaded all the models in a pipeline
and we store it in a python dictionary to loop over them one after the other.

**Naive Bayes**

We used multinomial NB (Naive Bayes)[3] to perform ‘transform’ on our data and we used
countvectorizer, feature selection and the model itself in our pipeline.
![](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Assignment%206%20DAta%2FScreen%20Shot%202018-07-30%20at%2010.10.28%20PM.png?alt=media&token=48322af8-8d31-476f-837a-bec07dcc0d31)

Code to save NB in pipeline [Figure 2]

Naive Bayes uses a prior data (known knowledge) to classify the data into different labels.
Since the data had more than two labels we went with Multinomial NB algorithm to perform
classification.

**Logistic Regression**

Logistic regression[4] is well known algorithm in classification. We played around with this
algorithm and figured that ‘newton-cg’ was solver for this particular dataset. Since, the
sigmoid and tanH functions were not giving us the accuracy we were expecting, we used
‘newton-cg’.

![](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Assignment%206%20DAta%2FScreen%20Shot%202018-07-30%20at%2010.09.51%20PM.png?alt=media&token=11057a78-0c43-4db1-be9b-a2630e0e493b)

Code to save Logistic Regression in pipeline [Figure 3]

**Decision Tree Classifier**

Usually Decision Tree[1] is used for predictive analysis, but it also has the capability to
perform classification. It one of widely used algorithm used in Machine Learning. It is the
foundation that runs the random forest classifier.

![](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Assignment%206%20DAta%2FScreen%20Shot%202018-07-30%20at%2010.10.19%20PM.png?alt=media&token=9873d3d3-ab37-47e0-a989-f4d448d80460)
Code to save Decision tree in pipeline [Figure 4]

**LinearSVC**

LinearSVC[2] uses the One-vs-All (also known as One-vs-Rest) multiclass reduction. It is
also noted here. Also, for multi-class classification problem SVC fits K \* (K - 1) / 2 models
where K is the amount of classes.

![](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Assignment%206%20DAta%2FScreen%20Shot%202018-07-30%20at%2010.09.51%20PM.png?alt=media&token=11057a78-0c43-4db1-be9b-a2630e0e493b)
Code to save LinearSVC in pipeline [Figure 5]

![](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Assignment%206%20DAta%2Fseaborn.png?alt=media&token=7cce2325-8682-40db-b351-f8998fe6523f)

### Pairplot [Figure 1]

## Output

**The Confusion Matrix of LinearSVC**

![](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Assignment%206%20DAta%2FLinearSVCHeatmap.png?alt=media&token=29da5767-d67f-45b4-bd76-342eeb39ed84)

Confusion Matrix of LinearSVC [Figure 6]

**The confusion Matrix for Decision Tree**

![](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Assignment%206%20DAta%2FDecision%20tree.png?alt=media&token=43a69102-3d01-4091-8c1b-8ce9a37ebdc5)

Confusion Matrix of Decision Tree [Figure 7]

**The confusion Matrix for Naive Bayes**

![](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Assignment%206%20DAta%2FNB.png?alt=media&token=7e26dd2d-281d-402c-94c0-0a5a82167c67)

Confusion Matrix of Naive Bayes [Figure 8]

**The confusion Matrix for Logistic Regression**

![](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Assignment%206%20DAta%2FLogisticRe.png?alt=media&token=02869df5-f7f6-416e-bc76-29092a658769)

Confusion Matrix of Logistic Regression [Figure 9]

## Accuracy Comparison

![](https://firebasestorage.googleapis.com/v0/b/assignment4-fc96b.appspot.com/o/Assignment%206%20DAta%2FScreen%20Shot%202018-07-30%20at%2011.16.16%20PM.png?alt=media&token=60377b3b-f414-4353-bcac-3b55ddc5ddba)
Accuracy of all models Train V Test [Figure 10]

We can clearly see that the accuracy of Naive Bayes was higher during the training
however the model didn’t perform that well when it saw unseen data. LinearSVC, on

the other hand, performed consistently across train and test data.

## Reference

[1] scikit-learn, "scikit-learn," [Online]. Available:
[http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#skle](http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#skle)
arn.tree.DecisionTreeClassifier. [Accessed 29 07 2018].

[2] "svc," [Online]. Available:
[http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html.](http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html.) [Accessed 29
07 2018].

[3] "naivebayes," [Online]. Available:
[http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html.](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html.)
[Accessed 29 07 2018].

[4] "logreg," [Online]. Available:
[http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.htm](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.htm)
l. [Accessed 29 07 18].
