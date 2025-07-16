din = True
senha = True
if din== True and senha == True:
    print('Saldo disponível')
elif din== True and senha == False:
    print('Senha errada')
elif din== False and senha == True:
    print('Saldo insuficiente')
elif din == False and senha == False:
    print('Dados incorreto')
# 