from random import choice


# para gerar passeis/walk aletorios
class RandomWalk():
    def __init__(self, numberPoints=5000):
        # atributos
        self.numberPoints = numberPoints

        # posicao do passeio/walk
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        # calcula os pontos do walk/passeio
        # continua dando passos no walk/passeio para alcancar o tamnaho

        while len(self.x_values) < self.numberPoints:

            # direção e distancia percorrida
            x_direction = choice([1, -1])
            x_distance = choice([0, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 2, 3, 4])
            y_step = y_direction * y_distance

            # rejeitar movimentos que não irão para nenhum lugar
            if x_step == 0 and y_step == 0:
                continue

            # calcular os valores proximos x y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
