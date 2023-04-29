frase = '       Olha que   , coisa interessante!'

lista_de_frases_cruas = frase.split(',')

lista_frases_fixed = []
for i, frase in enumerate(lista_de_frases_cruas):
    nova_frase = lista_de_frases_cruas[i].strip()
    lista_frases_fixed.append(nova_frase)

# print(lista_frases_fixed)

frases_unidas = ' '.join(lista_frases_fixed)
print(frases_unidas)
