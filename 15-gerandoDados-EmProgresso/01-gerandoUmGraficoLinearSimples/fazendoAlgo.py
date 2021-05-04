import matplotlib.pyplot as plt
from random import randint

tamanho = 30
algoAleatorio = [randint(1, tamanho) for _ in range(tamanho)]

print(algoAleatorio)


plt.plot(algoAleatorio)
plt.show()