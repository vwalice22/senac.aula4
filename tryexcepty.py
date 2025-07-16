try:
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        print('Par')
    else:
        print('Ímpar')
except ValueError:
    print('Digite um valor numérico válido.')
