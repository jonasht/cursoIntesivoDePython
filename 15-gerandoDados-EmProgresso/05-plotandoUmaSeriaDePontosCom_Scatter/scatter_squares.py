import matplotlib.pyplot as plt

x_values = [i for i in range(1, 6)]
y_values = [1,4,9, 16, 25]

plt.scatter(x_values, y_values, s=100)

# titulo do grafico e nomeiacao dos eixos
plt.title('square numbers', fontsize=24)
plt.xlabel('value', fontsize=14)
plt.ylabel('square of value', fontsize=14)

# tamanhos dos totulos de marcacao
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
