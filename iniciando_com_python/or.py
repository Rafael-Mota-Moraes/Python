entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123'

entrada_permitida = entrada == 'E' or entrada == 'e'

if entrada_permitida and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Tabela verdade do or
print(True or True)
print(True or False)
print(False or True)
print(False or False)
