import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('full_data.csv')
rd = df.to_dict('list')
longitud = len(rd['location'])  # hice esto para depues de esto hacer las listas generales de un pais
position = 1     # sirve para asignar posiciones a los graficos
countrytable = []    #lista con los nombres de todos los paises en el archivo
for k in range(0,longitud):                            #hace la lista con los nombres de los paises pero en minuscula asi es mas facil hacer que coincida el input.
    countrytable.append((rd['location'][k]).lower())

print('Deberá ingresar fechas con el formato ISO 8601 .Ej: 2020-05-07. Si el pais a ingresar tiene varias palabras tienen que estar separadas por un espacio.')

initialdate = (input('Ingrese fecha de inicio: '))
finaldate = (input('Ingrese fecha de final: '))

countries = []

while True:                    #valida el input de numero de paises a analizar
    try:
        inputnumbr = int(input('Ingrese la cantidad de paises a analizar: '))
        if inputnumbr < 0:
            raise Exception
    except Exception:
        print('Entrada invalida')
        continue
    else:
        break


for i in range(inputnumbr):            # ve si el input de pais es valido o no
    welcome = (input('Ingrese el país deseado: ')).lower()
    if welcome in countrytable:
        if welcome not in countries:
            countries.append(welcome)
        elif welcome in countries:
            print('ya eligio ese pais')
    else:
        print('Entrada no valida')

for country in countries:
    dates = []                 #aca se guardan todas las fechas de todo el pais en cuestion
    xdates = []                   #aca se guardan las fechas entre los valores elegidos
    indexinitialdate = None         #contiene el indice de la fecha inicial elegida
    indexfinaldate = None             #contiene el indice de la fecha final elegida
    totalcases = []             #aca se guardan todos los valores de casos totales del pais
    totaldeaths = []            #aca se guardan todos los valores de muertes totales del pais
    ytotalcases = []            # contiene los valores de casos totales entre las fechas elegidas
    ytotaldeaths = []           # contiene los valores de muertes totales entre las fechas elegidas
 
    for a in range(0,longitud):                  #hace listas de todos los datos (fechas,
        if (rd['location'][a]).lower() == country:    #contagiados y muertos) del pais     
            dates.append(rd['date'][a])                    
            totalcases.append(rd['total_cases'][a])
            totaldeaths.append(rd['total_deaths'][a])
    if (initialdate not in dates):             #soluciona el problema si la fecha inicial o final 
        initialdate = dates[0]              #elegidas no son una fecha que exista para tal pais en el .csv
        finaldate = dates[len(dates)-1]
    for b in range(0,len(dates)):                          #toma la posicion en la lista dates de la
            if dates[b] == initialdate:                    # fecha inicial y la final elegidas
                indexinitialdate = b                       
            elif dates[b] == finaldate:
                indexfinaldate = b
    for c in range(0,len(dates)):                            #hace listas de los datos entre las fechas elegidas
        if (indexinitialdate <= c) & (c <= indexfinaldate):  
            xdates.append(dates[c])
            ytotalcases.append(totalcases[c])
            ytotaldeaths.append(totaldeaths[c])

    plt.subplot(int((inputnumbr/2)+(inputnumbr%2)),2, position)   #asigna posiciones dependiendo de la cantidad de paises
    position += 1
    plt.ylabel('personas')         
    plt.yscale('log')  #hace que la escala sea logaritmica
    plt.plot(xdates, ytotalcases, label='contagiados')
    plt.plot(xdates, ytotaldeaths, label='fallecidos')
    plt.title('coronavirus en '+ country) #hace que el titulo sea el correcto para el grafico
    plt.xticks([xdates[0], xdates[len(xdates)-1]], visible=True, fontsize=5) #hace que solo se vea el primer valor y el ultimo valor de la escala en x
    plt.yticks(fontsize=6)

plt.legend()
plt.show()
print()