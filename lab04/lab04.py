# -*- coding: utf-8 -*-
"""lab04.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZFV1XaPdxDx_818YhiCwrHdCL40E2boX

1. Przygotowanie danych
"""

from sklearn import datasets
data_breast_cancer = datasets.load_breast_cancer(as_frame=True)
data_iris = datasets.load_iris(as_frame=True)

from sklearn.model_selection import train_test_split

X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(data_breast_cancer['data'][['mean smoothness', 'mean area']],data_breast_cancer['target'], test_size=0.2)
X_train_i, X_test_i, y_train_i, y_test_i = train_test_split(data_iris["data"], data_iris["target"], test_size=0.2)

"""3. Klasyfikacja (breast cancer)"""

from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
svm_cancer = Pipeline([("linear_svc", LinearSVC(C=1, loss="hinge"))])
svm_cancer_auto_scale = Pipeline([("scaler", StandardScaler()), ("linear_svc", LinearSVC(C=1, loss="hinge"))])

svm_cancer.fit(X_train_c, y_train_c)
svm_cancer_auto_scale.fit(X_train_c, y_train_c)

import pickle
acc_train = svm_cancer.score(X_train_c, y_train_c)
acc_auto_scale_train = svm_cancer_auto_scale.score(X_train_c, y_train_c)
acc_test = svm_cancer.score(X_test_c, y_test_c)
acc_auto_scale_test = svm_cancer_auto_scale.score(X_test_c, y_test_c)

data = [acc_train, acc_test, acc_auto_scale_train, acc_auto_scale_test]
print(data)

with open("bc_acc.pkl", 'wb') as f:
    pickle.dump(data, f)
# Przy automatycznym skalowaniu danych skuteczność modelu jest znacznie większa

"""4. Klasyfikacja (iris)"""

svm_iris = Pipeline([("linear_svc", LinearSVC(C=1, loss="hinge", random_state=42))])
svm_iris_auto_scale = Pipeline([("scaler", StandardScaler()), ("linear_svc", LinearSVC(C=1, loss="hinge", random_state=42))])

svm_iris.fit(X_train_i, y_train_i)
svm_iris_auto_scale.fit(X_train_i, y_train_i)

acc_train = svm_iris.score(X_train_i, y_train_i)
acc_auto_scale_train = svm_iris_auto_scale.score(X_train_i, y_train_i)
acc_test = svm_iris.score(X_test_i, y_test_i)
acc_auto_scale_test = svm_iris_auto_scale.score(X_test_i, y_test_i)

data = [acc_train, acc_test, acc_auto_scale_train, acc_auto_scale_test]
print(data)

with open("iris_acc.pkl", 'wb') as f:
    pickle.dump(data, f)