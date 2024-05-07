import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv('data_C02_emission.csv')


plt.figure()
data['CO2 Emissions (g/km)'].plot(kind="hist", bins=20)
plt.show()

data['Fuel Type'] = data['Fuel Type'].astype('category')
colors = {'Z': 'brown', 'X': 'red', 'E': 'blue', 'D': 'black'}

data.plot.scatter(x="Fuel Consumption City (L/100km)", y="CO2 Emissions (g/km)", c=data["Fuel Type"].map(colors), s=50)
plt.show()


data.boxplot(column='CO2 Emissions (g/km)', by='Fuel Type')
plt.show()


fuel_group = data.groupby('Fuel Type').size()
fuel_group.plot(kind ='bar', xlabel='Fuel Type', ylabel='Number of vehicles', title='Amt of vehicles by fuel type')
plt.show()


cylinder_group = data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
cylinder_group.plot(kind='bar', x=cylinder_group.index, y=cylinder_group.values, xlabel='Cylinders', ylabel='CO2 emissions (g/km)', title='CO2 emissions by num of cylinders')
plt.show()