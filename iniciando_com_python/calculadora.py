n1 = input('Digite o primeiro número: ')
n2 = input('Digite o segundo número: ')
operador = input('Digite o operador desejado: ')

try:
    n1 = int(n1)
    n2 = int(n2)

    if operador == '+':
        print(f'{n1} + {n2} = {n1 + n2}')
    elif operador == '-':
        print(f'{n1} - {n2} = {n1 - n2}')
    elif operador == '/':
        print(f'{n1} / {n2} = {n1 / n2}')
    elif operador == '*':
        print(f'{n1} * {n2} = {n1 * n2}')
    else:
        print('Digite um operador válido.')

except:
    print('Digite números válidos')

