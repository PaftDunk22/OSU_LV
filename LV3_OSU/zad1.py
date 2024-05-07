import pandas as pd 

data = pd.read_csv('data_C02_emission.csv')

length = len(data['Make'])
print("Dataframe:",length)

for col in data.columns:
    print(col,"is",data[col].dtype)

data['Vehicle Class'] = data['Vehicle Class'].astype('category')

print("Redovi s izostalim vrijednostima:", data.isnull().sum())
print("Duplicirane vrijednosti:", data.duplicated().sum())


least = data.nsmallest(3, 'Fuel Consumption City (L/100km)')
most = data.nlargest(3, 'Fuel Consumption City (L/100km)')

print("Most:")
print(most[['Make', 'Model', 'Fuel Consumption City (L/100km)']])
print("Least:")
print(least[['Make', 'Model', 'Fuel Consumption City (L/100km)']])


data_3 = data[(data['Engine Size (L)'] >= 2.5) & (data['Engine Size (L)'] <= 3.5)]
length_3 = len(data_3['Make'])
print("Motor izmedu 2.5 i 3.5 L:",length_3)

print("Avg C02:",data_3['CO2 Emissions (g/km)'].mean(), "g/km")


data_4 = data[(data['Make'] == 'Audi')]
length_4 = len(data_4['Make'])
print("Audi mjerenja:",length_4)

data_4 = data_4[(data_4['Cylinders'] == 4)]
print("Avg CO2 for 4 cylinders",data_4['CO2 Emissions (g/km)'].mean(), "g/km")


cylinders = data['Cylinders'].value_counts().sort_index()
print(cylinders)

cylinder_emission = data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
print("Cylinder emissions:\n",cylinder_emission)


diesel = data[(data['Fuel Type'] == 'D')]
petrol = data[(data['Fuel Type'] == 'Z')]

print("Diesel:\nAvg:", diesel['Fuel Consumption City (L/100km)'].mean(),", Median:", diesel['Fuel Consumption City (L/100km)'].median())
print("Diesel:\nAvg:", petrol['Fuel Consumption City (L/100km)'].mean(),", Median:", petrol['Fuel Consumption City (L/100km)'].median())


four_c_diesel = diesel[(diesel['Cylinders'] == 4)]
print("Most consuming 4 cylinder diesel:",four_c_diesel.nlargest(1, 'Fuel Consumption City (L/100km)'))


manuals = data[(data['Transmission'].str[0] == 'M')]
length = len(manuals['Make'])
print("Manuals:",length)


print(data.corr(numeric_only=True))
