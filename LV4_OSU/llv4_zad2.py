#Zadatak 4.5.2 Na temelju rješenja prethodnog zadatka izradite model koji koristi i kategoricku ˇ
#varijable „Fuel Type“ kao ulaznu velicinu. Pri tome koristite 1-od-K kodiranje kategorickih ˇ
#velicina. Radi jednostavnosti nemojte skalirati ulazne velicine. Komentirajte dobivene rezultate. ˇ
#Kolika je maksimalna pogreška u procjeni emisije C02 plinova u g/km? O kojem se modelu
#vozila radi?

from sklearn.preprocessing import OneHotEncoder
from sklearn import datasets
from sklearn . model_selection import train_test_split
from sklearn . preprocessing import MinMaxScaler
import sklearn . linear_model as lm
from sklearn . metrics import max_error
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("data_C02_emission.csv")

input = ["Engine Size (L)","Cylinders","Fuel Type","Fuel Consumption City (L/100km)","Fuel Consumption Hwy (L/100km)","Fuel Consumption Comb (L/100km)","Fuel Consumption Comb (mpg)","CO2 Emissions (g/km)"]
output = "CO2 Emissions (g/km)"

X = data[input]
y = data[output]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2,random_state=1)

ohe = OneHotEncoder()
X_train_encoded = ohe.fit_transform(X_train[["Fuel Type"]]).toarray()
X_test_encoded = ohe.fit_transform(X_test[["Fuel Type"]]).toarray()

linearModel = lm.LinearRegression()
linearModel.fit(X_train_encoded, y_train)

y_test_p = linearModel.predict(X_test_encoded)

ME = max_error(y_test, y_test_p)
print("ME:",ME)

error = np.abs(y_test, y_test_p)
print(y_test)

#print(np.max(error))
#max_error_id = np.argmax(error)

#max_error_model = data.iloc[max_error_id, 1]
#print(max_error_model)