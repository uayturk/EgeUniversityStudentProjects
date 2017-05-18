# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 13:27:45 2017

@author: King Info Tech
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.ensemble import RandomForestClassifier
import sklearn.metrics

data_train = pd.read_csv("datatraining.txt")
data_test = pd.read_csv("datatest.txt")

data_train.columns
data_train.head(5)
data_train.describe()
#print(data_train.columns)
#print(data_train.head(5))
#delete date column since we dont need it
data_train.drop(labels=['date'],axis=1,inplace=True)
#our estimation rely on Occupancy column
out_train = data_train['Occupancy']

#drop Occupance table in our input data
data_train.drop(labels=['Occupancy'],axis=1,inplace=True)
out_train = out_train.values
data_train= data_train.values
#print(data_train)
"""
Now lets clean our data test
"""
data_test.drop(labels=['date'],axis=1,inplace=True)
out_test = data_test['Occupancy']
data_test.drop(labels=['Occupancy'],axis=1,inplace=True)
inLabels = data_test.columns.tolist()
out_test = out_test.values
data_test = data_test.values

"""
"""
classifier = RandomForestClassifier(n_estimators=25,max_depth=3)
classifier = classifier.fit(data_train,out_train)

predictions = classifier.predict(data_test)

#cm= confusion matrix
cm=sklearn.metrics.confusion_matrix(out_test,predictions)

#acc = accuracy
acc=sklearn.metrics.accuracy_score(out_test,predictions)
#print(acc)
#cfi=classfier feature importance
cfi= classifier.feature_importances_
print(cfi)
"""
grafic presentation[Histogram]
"""
#x positons
x_pos = list(range(len(inLabels)))
print(x_pos)
plt.bar(x_pos,classifier.feature_importances_,align='center')
plt.grid()

max_y = max(classifier.feature_importances_)
plt.ylim([0,max_y*1.1])
plt.ylabel('Importance')
plt.xticks(x_pos, inLabels)
plt.title('Importance Of Features')
plt.show()





