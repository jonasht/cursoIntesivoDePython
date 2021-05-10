from random_walk import RandomWalk
import matplotlib.pyplot as plt

# criando um passeio/walk aleatorio e
# plotar os pontos
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=5, cmap=plt.cm.Greens)
plt.savefig('13-plotandoOPasseioAleatorio/foto.png', bbox_inches='tight')
plt.show()
