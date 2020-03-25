#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# 데이터 셋 로딩
iris = load_iris()
X = iris.data
y = iris.target

# 데이터 셋 구분
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.5)

# 머신러닝 셋팅
clf = RandomForestClassifier(n_estimators=10)

# 훈련
clf.fit(X_train, y_train)

# 예측
predicted = clf.predict(X_test)

# 정확도 예측
print(accuracy_score(predicted, y_test))

import os
import pickle
current_dir = os.getcwd()
with open(os.path.join(current_dir,'rf.pkl'), 'wb') as rf_model:
    pickle.dump(clf, rf_model, protocol=2)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    