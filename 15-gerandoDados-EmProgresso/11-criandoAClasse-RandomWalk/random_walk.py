from random import choice


# para gerar passeis/walk aletorios
class RandomWalk():
    def __init__(self, numberPoints):
        # atributos
        self.numberPoints = numberPoints

        # posicao do passeio/walk
        self.x_values = [0]
        self.y_values = [0]
