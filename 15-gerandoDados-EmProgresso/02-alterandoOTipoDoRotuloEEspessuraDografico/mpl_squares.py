import matplotlib.pyplot as plt


squares = [1, 4, 9, 16, 25, 30]
plt.plot(squares, linewidth=5)

# titulo do grafico e nome dos eixos
plt.title('Square numbers ', fontsize=15)
plt.xlabel('value', fontsize=15)

# tamanho dos rotulos das marcacoes
plt.tick_params(axis='both', labelsize=15)

plt.show()
