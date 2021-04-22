
my_foods = ['pizza', 'pavee', 'bolo de cenoura'] 

# fazendo copia da lista de maneira correta
friend_foods = my_foods[:] 


my_foods.append('cannoli') 
friend_foods.append('Sorvete') 

print("My favorite foods are\nMinha comida favorita eh:")
print(my_foods)

print("\nMy friend's favorite foods are\nas comidas favoritas dos meus amigos sao:")
print(friend_foods)
