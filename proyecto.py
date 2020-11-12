import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('full_data.csv')
rd = df.to_dict('list')
longitud = len(rd['location'])

xdates = []
ytotalcases = []
ytotaldeaths = []

print('Deberá ingresar fechas con el formato: año-mes-día (ej: 2020-05-07)')
welcome = (input('Ingrese el país deseado: ')).lower()
initialdate = (input('Ingrese fecha de inicio: '))
finaldate = (input('Ingrese fecha de final: '))
# timeinterval = in
for a in range(0,longitud):
    if (rd['location'][a]).lower() == welcome:
        xdates.append(rd['date'][a])
        ytotalcases.append(rd['total_cases'][a])
        ytotaldeaths.append(rd['total_deaths'][a])
# comentario
plt.figure(figsize=(12,5))
plt.xlabel('fechas')
plt.ylabel('personas en millones')
plt.yscale('log')
plt.plot(xdates, ytotalcases, 'g-', label='contagiados')
plt.plot(xdates, ytotaldeaths, 'r-', label='fallecidos')
plt.title('coronavirus en '+ welcome)
plt.xticks(xdates[::30], rotation=30)
plt.legend()
plt.show()
print()