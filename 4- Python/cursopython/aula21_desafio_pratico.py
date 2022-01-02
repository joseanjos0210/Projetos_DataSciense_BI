# DESAFIO:
# ========
# Criar variaveis para nome (str), idade (int),
# altura (float) e peso (float) de uma pessoa
# Criar variável com ano atual (int)
# Obter o ano de nascimento da pessoa (baseado na idade e ano atual)
# Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
# Exibir um texto com todos os valores na tela usado F-strings (com as chaves)

nome = 'Jose Antonio dos Anjos'
idade = 60
peso = 105
altura = 1.89
ano_atual = 2021
ano_nasc =  ano_atual - idade
imc = peso / (altura ** 2)

print('Meu nome é {} minha idade {}, o meu peso atual e de {} quilos, tenho a altura de {},'
      ' o ano atual é {}, meu ano de nascimento é {}, meu IMC é {:.2f}'.format(nome, idade,
      peso, altura, ano_atual, ano_nasc, imc))