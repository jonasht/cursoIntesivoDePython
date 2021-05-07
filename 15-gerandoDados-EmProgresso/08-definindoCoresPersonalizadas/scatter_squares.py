import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# definindo cores, qualquer cor pode ser coloca em ingles ou em formato RGB:
# plt.scatter(x_values, y_values, c='green', s=40, edgecolors='none')
plt.scatter(x_values, y_values, c=(0, 0, 0.8, s=40, edgecolors='none')

# titulo do grafico e nomeiacao dos eixos
plt.title('square numbers', fontsize=24)
plt.xlabel('value', fontsize=14)
plt.ylabel('square of value', fontsize=14)

# tamanhos dos totulos de marcacao
plt.tick_params(axis='both', which='major', labelsize=14)

# intervalo para cada eixo
plt.axis([0, 1100, 0, 1100000])

plt.show()
