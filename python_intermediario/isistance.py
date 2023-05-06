lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome', 'Luiz'}]

for item in lista:
    if isinstance(item, set):
        item.add(2)

    print(item, isinstance(item, (int, float)))
