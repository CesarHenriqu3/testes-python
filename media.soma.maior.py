LISTA = [
    {"Nome": "Cesar", "nota": 10},
    {"Nome": "sdldsalasdl", "nota": 8},
    {"Nome": "aluno 3", "nota": 2},
    {"Nome": "aluno 4", "nota": 5},
    {"Nome": "aluno 5", "nota": 7},
    {"Nome": "aluno 6", "nota": 1},
    {"Nome": "aluno 7", "nota": 3},
]
soma = 0
maior_nota = 0
media_das_notas = 0
soma_das_notas = 0

for valor in LISTA:
    if maior_nota < valor["nota"]:
        maior_nota = valor["nota"]
print(maior_nota)

for valor in LISTA:
    soma = soma + valor["nota"]
    media_das_notas = soma / len(LISTA)
print(int(media_das_notas))

for valor in LISTA:
    soma_das_notas = soma_das_notas + valor["nota"]
print(soma_das_notas)
