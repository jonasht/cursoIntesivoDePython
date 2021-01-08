
class User(): 
    
    def __init__(self, first_name, last_name, email, username, password):
        # cadastrando usuario
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.username = username
        self.password = password
        
        
    def describe_user(self): # descrever usuario
        print(f'     nome: {self.first_name}')
        print(f'sobrenome: {self.last_name}')
        print(f'    email: {self.email}')
        print(f' username: {self.username}')
        print(f' password: {self.password}')
        
    def greet(self):
        print(f'saudacoes {self.first_name} {self.last_name}')


class Admin(User):
    def __init__(self, first_name, last_name, email, username, password):
        super().__init__(first_name, last_name, email, username, password)
        privilages = []
        
    def show_privilages(self):
        print(f'\n privilegios:')
        for privilage in self.privilages:
            print(f'    -> {privilage}')
        print()
    
    
        
u1 = User('felipe', 'arcades', 'feliades@outlook.com', 'felip123', '123')

u1.describe_user()
u1.greet()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

admin = Admin('jonas', 'jon', 'jonas@outlook.com', 'jonas123', '123')
admin.describe_user()
admin.privilages = [
                    'pode adicionar post',
                    'pode deletar post',
                    'pode banir usuario'
                    ]
admin.show_privilages()
