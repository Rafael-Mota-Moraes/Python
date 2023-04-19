a = 'A'
b = 'B'
c = 1.1

string = 'a={0} a={0} b={nome1} c={nome2:.2f} a={0}'
formato = string.format(a, nome1=b, nome2=c)

print(formato)
