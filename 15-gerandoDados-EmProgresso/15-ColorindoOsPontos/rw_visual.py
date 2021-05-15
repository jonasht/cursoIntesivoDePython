from random_walk import RandomWalk
import matplotlib.pyplot as plt

# criando um passeio/walk aleatorio
while True:
    rw = RandomWalk()
    rw.fill_walk()
    # plt.scatter(rw.x_values, rw.y_values, s=5, cmap=plt.cm.Greens)
    plt.savefig('15-ColorindoOsPontos/foto.png', bbox_inches='tight')

    # fazendo os pontos serem coloridos
    point_number = list(range(rw.numberPoints))
    plt.scatter(rw.x_values, rw.y_values, c=point_number,
                cmap=plt.cm.Greens, edgecolors='none', s=15)

    plt.show()

    keep_running = input('make another walk: (Y/n)\nfazer outro passeio (S/n)')
    if keep_running == 'n':
        break
