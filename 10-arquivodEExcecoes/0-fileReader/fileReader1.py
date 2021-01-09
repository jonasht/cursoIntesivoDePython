# lendo um arquivo inteiro

with open('./pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip()) # .rstrip() eh p remover a linha em branca do final do .txt
