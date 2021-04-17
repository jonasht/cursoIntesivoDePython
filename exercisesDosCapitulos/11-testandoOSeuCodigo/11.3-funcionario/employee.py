class Employee():


    def __init__(self, nome, sobrenome, salarioAnual):
        self.nome = nome.title()
        self.sobrenome = sobrenome.title()
        self.salario = salarioAnual

    def give_raise(self, quanto=5000):
        self.salario += quanto
