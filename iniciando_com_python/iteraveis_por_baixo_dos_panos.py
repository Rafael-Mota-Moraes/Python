"""
Iterável -> str, rangel, outros...
Iterador -> Aquele que sabe entregar um valor por vez
next = me entregue o próximo valor
iter = me entregue seu iterador
"""

# numeros = range(0, 100, 20)

# for numero in numeros:
#     print(numero)

texto = 'Rafael'
iterador = iter(texto)

while True:
    try:
        print(next(iterador))
    except:
        break


