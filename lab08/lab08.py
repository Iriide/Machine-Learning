# -*- coding: utf-8 -*-
"""lab08.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V1G4j5-V14s8aMHD9PTHPmRuoe3ilvpF
"""

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
import pickle

"""1. Przygotowanie danych"""

data_breast_cancer = datasets.load_breast_cancer()
data_iris = datasets.load_iris()

"""2. Explained variance ratio"""

scaler = StandardScaler()
scaled_bc = scaler.fit_transform(data_breast_cancer["data"])

pca_bc = PCA(n_components=0.9)
reduced_bc = pca_bc.fit_transform(scaled_bc)

print(pca_bc.explained_variance_ratio_)
with open("pca_bc.pkl", "wb") as f:
    pickle.dump(pca_bc.explained_variance_ratio_, f)

scaled_ir = scaler.fit_transform(data_iris["data"])

pca_ir = PCA(n_components=0.9)
reduced_ir = pca_ir.fit_transform(scaled_ir)

print(pca_ir.explained_variance_ratio_)
with open("pca_ir.pkl", "wb") as f:
    pickle.dump(pca_ir.explained_variance_ratio_, f)

"""3. Components"""

components = pca_bc.components_
print(components)
indexes = []
for i in range(0, len(components)):
    indexes.append(np.argmax(abs(pca_bc.components_[i])))

print(indexes)
with open("idx_bc.pkl", "wb") as f:
    pickle.dump(indexes, f)

components = pca_ir.components_
print(components)
indexes = []
for i in range(0, len(components)):
    indexes.append(np.argmax(abs(pca_ir.components_[i])))

print(indexes)
with open("idx_ir.pkl", "wb") as f:
    pickle.dump(indexes, f)