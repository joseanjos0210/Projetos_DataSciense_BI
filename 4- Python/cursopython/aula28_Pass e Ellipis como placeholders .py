 # aula28_1_Pass e Ellipis como placeholders 

# exemplo

valor = True

if valor:
    pass      # Pass -> dados informativo provisoriamente  para inclusão da ação de fato que sera efetuada
else:
    print(' Ola execução da condição do else ok..')
    
    
## ou com Ellipis

if valor:
    ...      # Ellipis -> dados informativo provisoriamente  para inclusão da ação de fato que sera efetuada
else:
    print(' Ola execução da condição do else ok..')