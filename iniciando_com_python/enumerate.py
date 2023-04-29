lista = ['Maria', 'Helena', 'João']
lista.append('Marcelo')

lista_enumerada = list(enumerate(lista))

# print(next(lista_enumerada))
# print(next(lista_enumerada))
# print(next(lista_enumerada))

for item in lista_enumerada:
    indice, valor = item

    print(indice, valor)

print(lista_enumerada)
