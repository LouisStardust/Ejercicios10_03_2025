import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

try:
    ventas_df = pd.read_excel('proyecto1.xlsx')
    sucursales_df = pd.read_excel('Catalogo_sucursal.xlsx')
    print("Datos cargados")
except FileNotFoundError as e:
    print(f"Error: {e}")
    exit()

ventas_df = ventas_df.merge(sucursales_df, left_on='id_sucursal', right_on='id_sucursal')

ventas_totales = ventas_df['ventas_tot'].sum()
print(f"\n1. Ventas totales: ${ventas_totales:,.2f}")

socios_con_adeudo = ventas_df[ventas_df['B_adeudo'] == 'Con adeudo']['no_clientes'].sum()
socios_sin_adeudo = ventas_df[ventas_df['B_adeudo'] == 'Sin adeudo']['no_clientes'].sum()
total_socios = socios_con_adeudo + socios_sin_adeudo

print(f"\n2. Socios con adeudo: {socios_con_adeudo} ({socios_con_adeudo/total_socios:.1%})")
print(f"Socios sin adeudo: {socios_sin_adeudo} ({socios_sin_adeudo/total_socios:.1%})")

ventas_df['B_mes'] = pd.to_datetime(ventas_df['B_mes'])
ventas_por_mes = ventas_df.groupby(ventas_df['B_mes'].dt.to_period('M'))['ventas_tot'].sum()

plt.figure(figsize=(12,6))
ventas_por_mes.plot(kind='bar', color='purple')
plt.title('Ventas Totales por Mes')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('ventas_mes.png')

pagos_por_mes = ventas_df.groupby(ventas_df['B_mes'].dt.to_period('M'))['pagos_tot'].std()

plt.figure(figsize=(12,6))
pagos_por_mes.plot(kind='line', marker='o', color='yellow')
plt.title('Desviación Estándar de Pagos')
plt.xlabel('Mes')
plt.ylabel('Desviación Estándar')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('desviacion_pagos.png')

deuda_total = ventas_df['adeudo_actual'].sum()
print(f"\n5. Deuda total: ${deuda_total:,.2f}")

porcentaje_utilidad = (ventas_totales - deuda_total) / ventas_totales * 100
print(f"\n6. Porcentaje de utilidad: {porcentaje_utilidad:.2f}%")

ventas_por_sucursal = ventas_df.groupby('suc')['ventas_tot'].sum()

plt.figure(figsize=(10,8))
ventas_por_sucursal.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Ventas por Sucursal')
plt.ylabel('')
plt.tight_layout()
plt.savefig('ventas_sucursal.png')

resumen_sucursal = ventas_df.groupby('suc').agg({
    'ventas_tot': 'sum',
    'adeudo_actual': 'sum'
})
resumen_sucursal['margen'] = (resumen_sucursal['ventas_tot'] - resumen_sucursal['adeudo_actual']) / resumen_sucursal['ventas_tot'] * 100

fig, ax1 = plt.subplots(figsize=(12,6))
color = 'tab:blue'
ax1.set_xlabel('Sucursal')
ax1.set_ylabel('Deuda Total', color=color)
ax1.bar(resumen_sucursal.index, resumen_sucursal['adeudo_actual'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Margen de Utilidad', color=color)
ax2.plot(resumen_sucursal.index, resumen_sucursal['margen'], color=color, marker='o')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Deuda y Margen por Sucursal')
fig.tight_layout()
plt.savefig('deuda_y_margen_sucursal.png')

print("\nAnálisis completo, ya esta todo hecho")