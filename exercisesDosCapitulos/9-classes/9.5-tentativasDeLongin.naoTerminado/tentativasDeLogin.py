
class User(): 
    
    def __init__(self, first_name, last_name, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.login_attempts = 0
        
        
    def describe_user(self):
        print(f'nome: {self.first_name}')
        print(f'sobrenome: {self.last_name}')
        print(f'email: {self.email}')
        print(f'username: {self.username}')
        print(f'password: {self.password}')
        
    def greet(self):
        print(f'saudacoes {self.first_name} {self.last_name}')

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


u1 = User('felipe', 'arcades', 'feliades@outlook.com', 'felip123', '123')

u1.describe_user()
u1.greet()
print()


print('tentativas de longin:')
print(u1.login_attempts)

print('tentado fazer tentativas de longin 5 vezes')
for i in range(5):
    u1.increment_login_attempts()
    
print('tentativas de longin:')
print(u1.login_attempts)

for i in range(6):
    u1.increment_login_attempts()
        
print('tentativas de longin:')
print(u1.login_attempts)


print('--'*30)

