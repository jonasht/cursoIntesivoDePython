

from user import User

class Admin(): 
    
    def __init__(self, first_name, last_name, email, username, password):
        # cadastrando usuario
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.username = username
        self.password = password
        
        self.privilages = Privileges([])
        
    def describe_user(self): # descrever usuario
        print(f'\nDados:')
        print(f'         nome: {self.first_name}')
        print(f'    sobrenome: {self.last_name}')
        print(f'        email: {self.email}')
        print(f'     username: {self.username}')
        print(f'     password: {self.password}')
        

class Privileges():
    def __init__(self, privilages):
        self.privilages = privilages
        
    def show_privilages(self):
        print(f'\nprivilegios:')
        for privilage in self.privilages:
            print(f'    -> {privilage}')
        print()
    
    
        


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

