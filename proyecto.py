import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('full_data.csv')
rd = df.to_dict('list')
longitud = len(rd['location'])

dates = []
xdates = []
indexinitialdate = None
indexfinaldate = None
totalcases = []
totaldeaths = []
ytotalcases = []
ytotaldeaths = []

print('Deberá ingresar fechas con el formato: año-mes-día (ej: 2020-05-07)')
welcome = (input('Ingrese el país deseado: ')).lower()
initialdate = (input('Ingrese fecha de inicio: '))
finaldate = (input('Ingrese fecha de final: '))
for a in range(0,longitud):                            #hace listas de todos los datos (fechas,
    if (rd['location'][a]).lower() == welcome:         #contagaidos y muertos) del pais
        dates.append(rd['date'][a])
        totalcases.append(rd['total_cases'][a])
        totaldeaths.append(rd['total_deaths'][a])
for b in range(0,len(dates)):                          #toma la posicion en la lista dates de la
            if dates[b] == initialdate:                # fecha inicial y la final elegidas
                indexinitialdate = b
            elif dates[b] == finaldate:
                indexfinaldate = b
for c in range(0,len(dates)):                            #hace listas de los datos entre las fechas elegidas
    if (indexinitialdate <= c) & (c <= indexfinaldate):
                xdates.append(dates[c])
                ytotalcases.append(totalcases[c])
                ytotaldeaths.append(totaldeaths[c])

plt.figure(figsize=(12,5))
plt.xlabel('fechas')
plt.ylabel('personas en millones')
plt.yscale('log')
plt.plot(xdates, ytotalcases, 'g-', label='contagiados')
plt.plot(xdates, ytotaldeaths, 'r-', label='fallecidos')
plt.title('coronavirus en '+ welcome)
plt.xticks(xdates[::int(len(xdates)/20)], rotation=30)   # hace que la escala del eje x se vea mejor, no funciona bien para selecciones de intervalos de tiempo cortos
plt.legend()
plt.show()
print()