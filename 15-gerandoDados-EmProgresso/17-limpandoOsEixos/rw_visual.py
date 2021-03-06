from random_walk import RandomWalk
import matplotlib.pyplot as plt
# feito no gnu/linux fedora


# criando um passeio/walk aleatorio
while True:
    rw = RandomWalk()
    rw.fill_walk()
    # plt.scatter(rw.x_values, rw.y_values, s=5, cmap=plt.cm.Greens)
    plt.savefig('foto.png', bbox_inches='tight')

    # fazendo os pontos serem coloridos
    point_number = list(range(rw.numberPoints))
    plt.scatter(rw.x_values, rw.y_values, c=point_number,
                cmap=plt.cm.Greens, edgecolors='none', s=15)

    # enfatizar o primeiro e o ultimo ponto
    plt.scatter(0, 0, c='blue', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    
    # remover os eixos
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('make another walk: (Y/n)\nfazer outro passeio (S/n)')
    if keep_running == 'n':
        break
