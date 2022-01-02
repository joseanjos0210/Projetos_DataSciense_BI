# aula31_formatando_valores_com_modificadores

# Formatando valores com modificadores atual

# :s - Texto (strings)
# :d - Interiors (int)
# :f - Numeros de ponto flutuante (float) 
# :.(NUMERO)f - Quantidade de casas decimais (float)
# :(CARACTERE) (> ou  < ou ^) (QUANTIDADE/TIPO -s, d  ou f)

# > - Esquerda
# < - Direita
# ^ - Centro

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('Divisao de num_1 (10) por num_2 (3) ->>> ', divisao)
print( "Divisão com format (:.2f)  ->>> " '{:.2f}'.format(divisao) )

nome = 'José Antõnio'
num_int = 12345
num_fl = 1281567
num_9 = 999
print("Formatando com opção format f (nome:s) string ->>> " f'{nome:s}')

print("Formatando com opção format f (num_int:d) numeros inteiros ->>> " f'{num_int:d}')

print("Formatando com opção format f (num_fl:.2f) num_fl = 1281567  sera exibido com 2 casa decimais ->>> " f'{num_fl:.2f}')

print("Formatando com opção format f (num_9:0>10) sera exibido com zeros a esquerda juntamente num_9 = 999->>> " f'{num_9:0>10}')

print("Formatando com opção format f (num_9:0<10) sera exibido com zeros a direita juntamente num_9 = 999->>> " f'{num_9:0<10}')

print("Formatando com opção format f (num_9:0^10) sera exibido com zeros centralizando num_9 = 999->>> " f'{num_9:0^10}')

print("Formatando com opção format f (nome:#^50) sera exibido com 50 hashtag centralizando o conteudo da variavel nome ->>> " f'{nome:#^50}')