pessoa = {}

pessoa['nome'] = 'Rafael'
pessoa['sobrenome'] = 'Moreira'

del pessoa['sobrenome']

print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome', None) is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])
