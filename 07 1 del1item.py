

alien = {'cor': 'verde', 'pontos': 5}
alien['y_posicao'] = 25 # add posicao no dic
alien['x_posicao'] = 35

print('\nalien: ')
print(alien)

alien['cor'] = 'amarela'
print('\nalien modificado: ')
print(alien)

print('\ndeletando pontos')
del alien['pontos']
print(alien)




