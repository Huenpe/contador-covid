import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('full_data.csv')
rd = df.to_dict('list')
longitud = len(rd['location'])
position = 1
countrytable = []
for k in range(0,longitud):                            
    countrytable.append((rd['location'][k]).lower())

print('Deberá ingresar fechas con el formato ISO 8601 .Ej: 2020-05-07. Si el pais a ingresar tiene varias palabras tienen que estar separadas por un espacio.')

initialdate = (input('Ingrese fecha de inicio: '))
finaldate = (input('Ingrese fecha de final: '))

countries = []
cntrynumbr = int(input('Ingrese la cantidad de paises a analizar: '))
for i in range(cntrynumbr):
    welcome = (input('Ingrese el país deseado: ')).lower()
    if welcome in countrytable:
        if welcome not in countries:
            countries.append(welcome)
        elif welcome in countries:
            print('ya eligio ese pais')
    else:
        print('Entrada no valida')

for country in countries:
    dates = []
    xdates = []
    indexinitialdate = None
    indexfinaldate = None
    totalcases = []
    totaldeaths = []
    ytotalcases = []
    ytotaldeaths = []

    for a in range(0,longitud):                            #linea 39 a 43
        if (rd['location'][a]).lower() == country:         #hace listas de todos los datos (fechas,
            dates.append(rd['date'][a])                    #contagaidos y muertos) del pais
            totalcases.append(rd['total_cases'][a])
            totaldeaths.append(rd['total_deaths'][a])
    if (initialdate not in dates):              #linea 44 a 46, soluciona el problema si la fecha inicial o final 
        initialdate = dates[0]              #elegidas no son una fecha que exista para tal pais en el .csv
        finaldate = dates[len(dates)-1]
    for b in range(0,len(dates)):                          #linea 47 a 51
            if dates[b] == initialdate:                    #toma la posicion en la lista dates de la
                indexinitialdate = b                       # fecha inicial y la final elegidas
            elif dates[b] == finaldate:
                indexfinaldate = b
    for c in range(0,len(dates)):                            #linea 52 a 56
        if (indexinitialdate <= c) & (c <= indexfinaldate):  #hace listas de los datos entre las fechas elegidas
            xdates.append(dates[c])
            ytotalcases.append(totalcases[c])
            ytotaldeaths.append(totaldeaths[c])

    plt.subplot(int((cntrynumbr/2)+(cntrynumbr%2)),2, position)
    position += 1
    plt.ylabel('personas en millones')
    plt.yscale('log')
    plt.plot(xdates, ytotalcases, label='contagiados')
    plt.plot(xdates, ytotaldeaths, label='fallecidos')
    plt.title('coronavirus en '+ country)
    plt.xticks([xdates[0], xdates[len(xdates)-1]], visible=True, fontsize=5)
    plt.yticks(fontsize=6)

plt.legend()
plt.show()
print()