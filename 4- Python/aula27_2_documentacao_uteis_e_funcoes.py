 #27-2 Aula teorica de Documentação e funções built-in úteis

# definindo as seguinte funções  is_float()  is_int()  is_number()
import re

def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
    return False

def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True
    return False

def is_number(val):
    return is_int(val) or is_float(val)

# atividade  de calculadora abaixo:

num_1= input('digite um número: ')
num_2= input('digite outro número: ')

# isnumeric()  isdigit()  isdecimal()
# os números devem serem possitivos (12345678) *** não podem ser float, números negativos,

print(num_1.isnumeric())
print(num_2.isnumeric())
print()

if is_number(num_1) and is_number(num_2):
    num_1 = float(num_1)
    num_2 = float(num_2)
    print(num_1 +num_2)
    print()
else:
    print('Nãa consegui efetuar a conversão numerica para realizar o calculo.')
    print()

##---------------------------------------------
## Muito parecido com  if  ->  try:  e except:
##---------------------------------------------

try:
    num_1 = float(num_1)
    num_2 = float(num_2)
    print(num_1 +num_2)
    print()
except:
    print('Nãa consegui efetuar a conversão numerica para realizar o calculo.')
    print()


###########
#  USAGE  #
###########

# Float
print(is_float('-101.0112'))  # True
# Int

print(is_int('-1010112'))  # True
# Numbers in general (float ou int)

print(is_number('-1010.112'))  # True
# False
