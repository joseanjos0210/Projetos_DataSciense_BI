# aula32_indices_e_fatiamento_strings_python.py

# * Manipulando strings
# * String indices
# * Fatiamento de strings [inicio:fim:passo]
# Funções built-in len, abs, type, print, etc ...
# Essas funções podem ser usadas diretamente em cada tipo.

# Voce pode conferir  tudo isso em:
# https://docs.python.org/3/library/stdtypes.html  (tipos built-in)
# https://docs.python.org/3/library/functions.html (funções built-in)

# 'modo positivo Python s2' contem [012345678]  = tabela de indice (+)
# 'modo negativo Python s2' contem [987654321]  = tabela de indice (-)
texto = 'Python s2'

print('(modo positivo Python s2) contem [012345678]  = tabela de indice (+)')
print(
    'Fatiamento  do indice positivo na posição [2] da variavel texto (Py [t] hon s2) --->>>', texto[2])
print(
    'Fatiamento  do indice positivo na posição [8] da variavel texto (Python s [2] ) --->>>', texto[8])

print()
url = 'www.google.com.br/'
print('O conteudo de url ->>> ', url)
print(
    '(modo negativo de (www.google.com.br/) contem [181716151413121110987654321]  = tabela de indice (-)')
print(
    'Fatiamento do indice negativo a posição [:-1] da variavel url = (www.google.com.br [ / ]) --->>> ', url[:-1])
print(
    'Fatiamento do indice negativo na posição [-18:-15] da variavel url = ( [ www. ]google.com.br/) --->>> ', url[-18:-15])
print(
    'Fatiamento do indice positivo na posição [4:18] da variavel url = (www.[ google.com.br/ ]) --->>> ', url[4:18])
print()
print('Fução len(url) para informar quantos carater tem na variavel url = (www.google.com.br/) --->>> ', len(url))
print('Fução len(url) para informar quantos carater tem na variavel url = (www.google.com.br/) --->>> ', len(url))
print('Imprima o conteudo len(url) na vertical --->>> ', len(url))
for letra in url:
    print(letra)
