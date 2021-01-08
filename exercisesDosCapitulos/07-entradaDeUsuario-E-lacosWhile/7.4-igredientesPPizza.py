# ingredientes par uma pizza
i = 0
ings = []
while 1:
    
    ing = str(input('\nescreva quit p/ sair\nqual ingrediente queres:'))
    if ing == "quit": break
    ings.append(ing)
    for m_ings in ings:
        print(f'{i}-{m_ings}')
        i += 1
    i=0

    
    