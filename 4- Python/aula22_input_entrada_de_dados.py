# Entrada de dados de  Input

nome = input(' Qual o seu nome? ')
idade = input (' Qual sua idade: ')
ano_nasc = 2021-int(idade)

print()
print(f' O usuário digitou {nome}, e o tipo da variavél é '
      f'{type(nome)}')
print()
print(f'{nome} tem {idade} anos.')
print(f'{nome} nasceu no ano de {ano_nasc}.')
print()

numero_1 = input(' Digite um número : ')
numero_2 = input(' Digite outro número : ')
print(numero_1 + numero_2)                   # resultando concaternando  2+2  -> 22
print(int(numero_1) + int(numero_2))         # resultando na adição de  dois numero inteiros

