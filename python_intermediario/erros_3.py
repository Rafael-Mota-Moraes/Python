# raise - lançando exceções (erros)

# print(1/0)

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Divisão por zero é inválida')

    return True


def divide(n, d):
    nao_aceito_zero(d)
    return n / d


# print(123)
# raise ValueError('Deu erro')
# print(456)


print(divide(8, 0))
