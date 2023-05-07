import sys

iterable = ['Eu', 'tenho', '__iter__']
iterator = iter(iterable)
lista = [n for n in range(10000)]
generator = (n for n in range(10000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))
print(next(generator))
