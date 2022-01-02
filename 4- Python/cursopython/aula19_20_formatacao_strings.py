# introdução de formatação de strings

nome = 'Luiz Antonio de Souza' # string
idade = 32  # int
altura = 1.80  # float
peso = 80
imc = peso /(altura ** 2)    #  peso divido por altura ao quadro exponenciação 2

# formatação não padrão em python
print( nome, 'tem', idade, 'de idade e seu IMC é', imc)

# formatação de strings para melhor leitura e padrão python
print(f'{nome} tem {idade}, anos de idade e seu IMC é {imc:.2f}')   # :.2f  formatar com duas casas decimais

# outro tipo de formatação  em python
print('{} tem {}, anos de idade e seu IMC é {:.2f}'.format(nome, idade, imc))

# outro tipo de formatação  em python
print('{n} tem {i}, anos de idade e seu IMC é {c:.2f}'.format(n=nome, i=idade, c=imc))