from matplotlib import pyplot

numeros = list(i for i in range(1, 6))
cubos = list(i**3 for i in range(1, 6))
print(cubos)

pyplot.scatter(numeros, cubos, s=40, edgecolor='none')



# titulo do grafico e nomeiacao dos eixos
pyplot.title('numeros de quadros', fontsize=24)
pyplot.xlabel('valor', fontsize=14)
pyplot.ylabel('quadro de valor', fontsize=14)

pyplot.tick_params(axis='both', which='major', labelsize=14)

pyplot.show()
