string = 'Rafael'
# print(dir(string))

if hasattr(string, 'upper'):
    print('Existe o método upper')
    print(getattr(string, 'upper'))
