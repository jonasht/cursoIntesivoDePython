
class User(): 
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def describe_user(self):
        print(f'nome: {self.first_name}')
        print(f'sobrenome: {self.last_name}')
    def greet(self):
        print(f'saudacoes {self.first_name} {self.last_name}')

u1 = User('felipe', 'arcades')
u2 = User('jorge', 'nunes')
u3 = User('sonia', 'mardes')

u1.describe_user()
u1.greet()

u2.describe_user()
u2.greet()

u3.describe_user()
u3.greet()

print('--'*30)

