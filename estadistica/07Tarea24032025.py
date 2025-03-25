import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv('./estadistica/proyecto1.csv')
df2 = pd.read_csv('./estadistica/Catalogo_sucursal.csv')

df1["ventas_tot"] = pd.to_numeric(df1["ventas_tot"], errors="coerce")
ventas_totales = df1["ventas_tot"].sum()
print("Ventas totales:", ventas_totales)