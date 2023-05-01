x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


# def soma(x, y):
#     return x + y


def soma(*args):
    args = list(args)
    total = 0

    for num in args:
        total += num

    return total


soma_1 = soma(1, 2, 3, 4, 5, 6)
print(soma_1)

soma_2 = soma(10, 20, 30, 40)
print(soma_2)

outra_soma = soma(1, 2, 34, 5, 6, 77, 6, 5, 4, 3, 12, 10)
print(outra_soma)

print('Função sum(): ', sum([1, 2, 34, 5, 6, 77, 6, 5, 4, 3, 12, 10]))
