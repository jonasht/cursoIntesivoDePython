import matplotlib.pyplot as plt

input_values = [i for i in range(1, 6)]
print(input_values)
squares = [1, 4, 9, 16, 25]

plt.plot(input_values, squares, linewidth=5)

# titulo do grafico e nome dos eixos
plt.title('Square numbers ', fontsize=14)
plt.xlabel('value', fontsize=14)
plt.ylabel('square of value', fontsize=14)

# tamanho dos rotulos das marcacoes
plt.tick_params(axis='both', labelsize=14)

plt.show()
