import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('./estadistica/housing.csv')

#primeros 5
print (df.head())

#ultimos 5
print(df.tail())

#fila en especifico
print(df.iloc[7])

#columna por su nombre
print(df["ocean_proximity"])

#la media de la columna del total de cuartos
mediacuartos= df["total_rooms"].mean()
print('Media del total de cuartos:', mediacuartos)

#la mediana de la columna population
medianapopularidad= df["population"].median()
print('Mediana de popularidad:', medianapopularidad)

std_age = df["housing_median_age"].std()
print('Desviacion estandar en Años:', std_age)

#para poder filtrar
filtrodeloceano= df[df['ocean_proximity'] == "ISLAND"]
print('Filtro de proximidad del oceano:' , filtrodeloceano)

#vamos a crear un grafico de dispersion entre los registros de la proximidad del oceano vs los precios

plt.scatter(df["ocean_proximity"][:10], df["median_house_value"][:10])

#hay que definir a X y a Y
plt.xlabel('Proximidad')
plt.ylabel('Precio')
plt.title('Grafico de Dispersion de Proximidad al oceano vs Precio')
plt.show()