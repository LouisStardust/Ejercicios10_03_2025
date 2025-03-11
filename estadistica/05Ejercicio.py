import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('./estadistica/housing.csv')

media = df['median_house_value'].mean()
print("Media: ", media)
moda = df['median_house_value'].mode()
print("Moda: ", moda)
mediana = df['median_house_value'].median()
print("Mediana: ", mediana)
rango = df['median_house_value'].max()
print("Rango: ", rango)
varianza = df['median_house_value'].var()
print("Varianza: ", varianza)
desviacion = df['median_house_value'].std()
print("Desviacion estandar: ", desviacion)
