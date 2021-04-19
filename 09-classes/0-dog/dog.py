class Dog():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self): # sentar
        print(self.name.title() + ' estah agora sentado')
        
    def roll_over(self): # rolar
        print(self.name.title() + ' estah agora rolando')


my_dog = Dog('negao', 12)
your_dog = Dog('pintado', 14)


print()
print('-'*40)
print('o nome do meu cachorro eh ' + my_dog.name)
print('e tem ' + str(my_dog.age) + ' anos de idade')

print('-'*40)

my_dog.sit()
my_dog.roll_over()

print('-'*40)
print('o nome do seu cachorro eh ' + your_dog.name)
print('e tem ' + str(your_dog.age) + ' anos de idade')

print('-'*40)

your_dog.sit()
your_dog.roll_over()