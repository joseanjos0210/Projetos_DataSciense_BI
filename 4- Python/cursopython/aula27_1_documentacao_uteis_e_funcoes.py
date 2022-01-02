# 27 Aula teorica de Documentação e funções built-in úteis


num_1= input('digite um número: ')
num_2= input('digite outro número: ')

# isnumeric()  isdigit()  isdecimal()
# os números devem serem possitivos (12345678) *** não podem ser float, números negativos,

print(num_1.isnumeric())
print(num_2.isnumeric())
print()

if num_1.isdigit() and num_2.isdigit():
    num_1 = int(num_1)
    num_2 = int(num_2)
    print(num_1 +num_2)
else:
    print('Nãa consegui efetuar a conversão numerica para realizar o calculo.')

