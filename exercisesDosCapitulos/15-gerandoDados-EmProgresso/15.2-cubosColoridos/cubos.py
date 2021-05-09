import matplotlib.pyplot as plt

numeros = list(range(1, 6600))
cubos = list(i**3 for i in numeros)

plt.scatter(numeros, cubos, c=cubos, 
            cmap=plt.cm.Greens, 
            s=30, edgecolors='none')

# titulo do grafico e nomeiacao dos eixos
plt.title('numeros de quadro', fontsize=24)
plt.xlabel('valor', fontsize=14)
plt.ylabel('valorDeQuadros', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 6600, 0, 6600**3])

plt.savefig('cubosColoridos.png', bbox_inches='tight')
plt.show()
