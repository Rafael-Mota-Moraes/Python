try:
    # 1 / 1
    1 / 0
except ZeroDivisionError:
    print('Divisão por zero')
else:
    print('Ocorreu sem erros')
finally:
    print('Sempre será executado')
