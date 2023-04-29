salas = [
    ['Maria', 'Helena'],
    ['Helaine'],
    ['Luiz', 'João', 'Eduarda']
]

print(salas[2][1])

for sala in salas:
    for aluno in sala:
        print(aluno, end=' ')
