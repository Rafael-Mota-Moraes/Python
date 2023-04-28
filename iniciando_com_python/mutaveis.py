# nome = 'Rafael'
# outra_variavel = nome
# nome = 'João'

# print(nome)
# print(outra_variavel)

lista_a = ['Rafael', 'Luiz']
# lista_b = [*lista_a]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'

print(lista_b)
