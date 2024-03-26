#Zadatak 4.5.1 Skripta zadatak_1.py ucitava podatkovni skup iz ˇ data_C02_emission.csv.
#Potrebno je izgraditi i vrednovati model koji procjenjuje emisiju C02 plinova na temelju ostalih numerickih ulaznih velicina. Detalje oko ovog podatkovnog skupa mogu se pronaci u 3. ´
#laboratorijskoj vježbi.
#a) Odaberite željene numericke velicine specificiranjem liste s nazivima stupaca. Podijelite
#podatke na skup za ucenje i skup za testiranje u omjeru 80%-20%. ˇ
#b) Pomocu matplotlib biblioteke i dijagrama raspršenja prikažite ovisnost emisije C02 plinova ´
#o jednoj numerickoj velicini. Pri tome podatke koji pripadaju skupu za ucenje oznacite ˇ
#plavom bojom, a podatke koji pripadaju skupu za testiranje oznacite crvenom bojom. ˇ
#c) Izvršite standardizaciju ulaznih velicina skupa za ucenje. Prikažite histogram vrijednosti ˇ
#jedne ulazne velicine prije i nakon skaliranja. Na temelju dobivenih parametara skaliranja ˇ
#transformirajte ulazne velicine skupa podataka za testiranje. ˇ
#d) Izgradite linearni regresijski modeli. Ispišite u terminal dobivene parametre modela i
#povežite ih s izrazom 4.6.
#e) Izvršite procjenu izlazne velicine na temelju ulaznih velicina skupa za testiranje. Prikažite ˇ
#pomocu dijagrama raspršenja odnos izmedu stvarnih vrijednosti izlazne velicine i procjene ˇ
#dobivene modelom.
#f) Izvršite vrednovanje modela na nacin da izracunate vrijednosti regresijskih metrika na ˇ
#skupu podataka za testiranje.
#g) Što se dogada s vrijednostima evaluacijskih metrika na testnom skupu kada mijenjate broj ¯
#ulaznih velicina?

from sklearn import datasets
from sklearn . model_selection import train_test_split
from sklearn . preprocessing import MinMaxScaler
import sklearn . linear_model as lm
from sklearn . metrics import mean_absolute_error
from sklearn . metrics import mean_squared_error
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data_C02_emission.csv")

input = ["Engine Size (L)","Cylinders","Fuel Consumption City (L/100km)","Fuel Consumption Hwy (L/100km)","Fuel Consumption Comb (L/100km)","Fuel Consumption Comb (mpg)","CO2 Emissions (g/km)"]
output = "CO2 Emissions (g/km)"

X = data[input]
y = data[output]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2,random_state=1)

plt.scatter(X_train["Engine Size (L)"], y_train, color="Red")
plt.scatter(X_test["Engine Size (L)"], y_test, color="Blue")
plt.xlabel("Engine Size (L)")
plt.ylabel("CO2 Emissions (g/km)")
plt.title("b)")
plt.show()

plt.hist(X_train["Engine Size (L)"])
plt.xlabel("Engine Size (L)")
plt.ylabel("CO2 Emissions (g/km)")
plt.title("c) non-scaled")
plt.show()

sc = MinMaxScaler()
X_train_n = sc.fit_transform(X_train)
plt.hist
plt.hist(X_train_n[:, 0])
plt.xlabel("Engine Size (L)")
plt.ylabel("CO2 Emissions (g/km)")
plt.title("c) scaled")
plt.show()

X_test_n = sc.transform(X_test)

linearModel = lm.LinearRegression()
linearModel.fit(X_train_n, y_train)
print(linearModel.coef_)

y_test_p = linearModel.predict(X_test_n)
plt.scatter(y_test, y_test_p)
plt.xlabel("Real")
plt.ylabel("Predicted")
plt.title("e)")
plt.show()

MSE = mean_squared_error(y_test,y_test_p)
RMSE = mean_squared_error(y_test,y_test_p, squared=False)
MAE = mean_absolute_error(y_test,y_test_p)

print("f) MSE:" ,MSE,", RMSE:" ,RMSE,", MAE:" ,MAE)
