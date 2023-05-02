def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao} {nome}'

    return saudar


s1 = criar_saudacao('Bom dia', 'Rafael')
s2 = criar_saudacao('Boa noite', 'Rafael')
print(s1())
print(s2())
