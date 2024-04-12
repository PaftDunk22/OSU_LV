#Zadatak 5.5.1 Skripta zadatak_1.py generira umjetni binarni klasifikacijski problem s dvije
#ulazne velicine. Podaci su podijeljeni na skup za ucenje i skup za testiranje modela. ˇ
#a) Prikažite podatke za ucenje u ˇ x1 −x2 ravnini matplotlib biblioteke pri cemu podatke obojite ˇ
#s obzirom na klasu. Prikažite i podatke iz skupa za testiranje, ali za njih koristite drugi
#marker (npr. ’x’). Koristite funkciju scatter koja osim podataka prima i parametre c i
#cmap kojima je moguce definirati boju svake klase.
#b) Izgradite model logisticke regresije pomo ˇ cu scikit-learn biblioteke na temelju skupa poda- ´
#taka za ucenje. ˇ
#c) Pronadite u atributima izgradenog modela parametre modela. Prikažite granicu odluke ¯
#naucenog modela u ravnini ˇ x1 − x2 zajedno s podacima za ucenje. Napomena: granica ˇ
#odluke u ravnini x1 −x2 definirana je kao krivulja: θ0 +θ1x1 +θ2x2 = 0.
#d) Provedite klasifikaciju skupa podataka za testiranje pomocu izgradenog modela logisticke ˇ
#regresije. Izracunajte i prikažite matricu zabune na testnim podacima. Izracunate to ˇ cnost, ˇ
#preciznost i odziv na skupu podataka za testiranje.
#e) Prikažite skup za testiranje u ravnini x1 −x2. Zelenom bojom oznacite dobro klasificirane
#primjere dok pogrešno klasificirane primjere oznacite crnom bojom.

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn . linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report


X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

plt.scatter(X_train[:,0], y_train, c="blue")
plt.scatter(X_train[:,1], y_train, c="blue")
plt.scatter(X_test[:,0], y_test, c="red", marker='x')
plt.scatter(X_test[:,1], y_test, c="red", marker='x')
plt.title('a)')
plt.show()

LogRegression_model=LogisticRegression()
LogRegression_model.fit(X_train, y_train)
y_test_p = LogRegression_model . predict ( X_test )

b=LogRegression_model.intercept_
m1,m2=LogRegression_model.coef_.T

x=-m1/m2

xdim = np.array([-4, 4])
y=x*xdim+b
plt.plot(xdim,y,'k', lw=1, ls='--')
plt.show()
