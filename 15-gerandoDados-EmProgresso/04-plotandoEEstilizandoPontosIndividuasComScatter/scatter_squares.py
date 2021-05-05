import matplotlib.pyplot as plt

plt.scatter(2, 4, s=200)

# titulo do grafico e nomeiacao dos eixos
plt.title('square numbers', fontsize=24)
plt.xlabel('value', fontsize=14)
plt.ylabel('square of value', fontsize=14)

# tamanhos dos totulos de marcacao
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
