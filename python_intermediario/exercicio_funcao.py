def multiplica(*args):
    total = 1

    for num in args:
        total *= num

    return total


multiplicacao = multiplica(1, 2, 3, 4, 5)
print(multiplicacao)


def e_par(num):
    if num % 2 == 0:
        print('É par')
    else:
        print('É impar')


e_par(3)
e_par(2)
