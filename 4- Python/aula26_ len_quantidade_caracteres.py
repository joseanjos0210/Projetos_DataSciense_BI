#  len - Quantidade de caracteres

usuario = input('Digite seu Usuário: ')
print()
sexo= input('Digite seu sexo: ')
qtd_caracteres = len(usuario)

print()
print(usuario, qtd_caracteres, type(qtd_caracteres))
print()
if qtd_caracteres < 6:
    print('Você precisa digitar pelo meno 6 caracteres')
else:
    print('Voce foi cadastrado no sistema')
    print()
print(f'A quantidade total de caracteres digitados foi {len(usuario) + len(sexo)}')