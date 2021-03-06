import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values,
            cmap=plt.cm.Blues, s=40, edgecolors='none')
# salvando os graficos automaticamente
plt.savefig('squares_plot.png', bbox_inches='tight')
""" ele .savefig() salva automaticamente os graficos em PNG,
na parte inicial de ondo o codigo é executado, não na parte onde o codigo estah,
caso o codigo não seja executado na sua propria pasta..."""


# titulo do grafico e nomeiacao dos eixos
plt.title('square numbers', fontsize=24)
plt.xlabel('value', fontsize=14)
plt.ylabel('square of value', fontsize=14)

# tamanhos dos totulos de marcacao
plt.tick_params(axis='both', which='major', labelsize=14)

# intervalo para cada eixo
plt.axis([0, 1100, 0, 1100000])

plt.show()
