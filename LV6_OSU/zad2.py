import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV

# ucitaj podatke
data = pd.read_csv("Social_Network_Ads.csv")

# dataframe u numpy
X = data[["Age","EstimatedSalary"]].to_numpy()
y = data["Purchased"].to_numpy()

# podijeli podatke u omjeru 80-20%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify=y, random_state = 10)

# skaliraj ulazne velicine
sc = StandardScaler()
X_train_n = sc.fit_transform(X_train)
X_test_n = sc.transform((X_test))

KNN_model = KNeighborsClassifier(n_neighbors=5)
KNN_model.fit(X_train_n, y_train)
y_test_p_KNN = KNN_model.predict(X_test_n)
y_train_p_KNN = KNN_model.predict(X_train_n)

scores = cross_val_score(KNN_model, X_train, y_train, cv=5)
print(scores)

array = np.arange(1, 101)
param_grid = {'n_neighbors':array}
knn_gscv = GridSearchCV(KNeighborsClassifier(), param_grid , cv=5, scoring ='accuracy', n_jobs =-1)
knn_gscv.fit(X_train, y_train)
print(knn_gscv.best_params_)
print(knn_gscv.best_score_)
print(knn_gscv.cv_results_)