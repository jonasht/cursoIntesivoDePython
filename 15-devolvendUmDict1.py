# devolvendo um dicionario

def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age']=age
    return person

musian = build_person('jonas', 'hendrix', 25)
print(musian)

musian = build_person('jonas', 'hendrix')
print(musian)
