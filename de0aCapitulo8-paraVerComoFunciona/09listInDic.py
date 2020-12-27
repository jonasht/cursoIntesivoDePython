# uma lista dentro do dicionario
import colorama
colorama.init()# p/ funcionar no windows, linux funciona normalmente


g = '\033[32m' # green
f = '\33[m'

pizza = {
    'crust': 'think',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f'{g}\nyou ordered a ' + pizza['crust'] + '-crust pizza without gluten and soy:', f)
for topping in pizza['toppings']:
    print(f'\t {topping}')




