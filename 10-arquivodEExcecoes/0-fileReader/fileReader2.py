# lendo dados linha a linha

fileName = 'pi_digits.txt'

with open(fileName) as file_object:
    for line in file_object:
        print(line)