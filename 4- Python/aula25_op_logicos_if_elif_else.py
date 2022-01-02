# Operadores relacionais 
# == > >=  < <= !=

num_1 = 2
num_2 = '2'
expressao = (f' num_1=[2] == num_2=["2"] ->',  num_1 == num_2, "num_1 =>", type(num_1), "num_2=>", type(num_2))
print(expressao)
print()

num_1 = 2
num_2 = 2
expressao = (f' num_1=[2] == num_2=[2] ->',  num_1 == num_2, "num_1 =>", type(num_1), "num_2=>", type(num_2))
print(expressao)
print()


num_1 = 2
num_2 = 3
expressao = (f' num_1=[2] > num_2=[3] ->',  num_1 >= num_2, "num_1 =>", type(num_1), "num_2=>", type(num_2))
print(expressao)
print()

num_1 = 3
num_2 = 3
expressao = (f' num_1=[3] => num_2=[3] ->',  num_1 >= num_2, "num_1 =>", type(num_1), "num_2=>", type(num_2))
print(expressao)
print()

num_1 = 3
num_2 = 2
expressao = (f' num_1=[3] < num_2=[2] ->',  num_1 < num_2, "num_1 =>", type(num_1), "num_2=>", type(num_2))
print(expressao)
print()

num_1 = 3
num_2 = 3
expressao = (f' num_1=[3] <= num_2=[3] ->',  num_1 <= num_2, "num_1 =>", type(num_1), "num_2=>", type(num_2))
print(expressao)
print()

num_1 = 3
num_2 = 4
expressao = (f' num_1=[3] != num_2=[4] ->',  num_1 != num_2, "num_1 =>", type(num_1), "num_2=>", type(num_2))
print(expressao)
print()

nome = input(' Qual o seu nome ? : ')
idade = input(' Qual a sua idade? : ')

#limite para pegar emprestimo
idade_menor = 18
idade_maior = 69 # limite não pode pegar emprestimo
idade = int(idade)

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} você pode pegar o empréstimo.') 
else:
    print(f' {nome} **NÃO** pode pegar o empréstimo.')
    
    
    
    