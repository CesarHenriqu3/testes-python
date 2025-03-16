LISTA = [
    {"Nome": "Cesar", "nota": 10},
    {"Nome": "juninho", "nota": 8},
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

for valor in LISTA: # Buscar maior valor
    if maior_nota < valor["nota"]:
        maior_nota = valor["nota"]
print("A maior nota é:",maior_nota)

for valor in LISTA: # Buscar média
    soma = soma + valor["nota"]
    media_das_notas = soma / len(LISTA)
print("A média entre as notas é",int(media_das_notas))

for valor in LISTA: # Buscar soma das notas
    soma_das_notas = soma_das_notas + valor["nota"]
print("A soma das notas é:",soma_das_notas)

buscar_aluno = input("Busque um aluno: ") # Solicita o nome do aluno ao usuário

# Verificar se o aluno está na lista
for aluno in LISTA:
    if aluno["Nome"] == buscar_aluno:  # Comparação case-insensitive
        print(f'Nome: {aluno["Nome"]}, Nota: {aluno["nota"]}')
        break
else:
    print("Aluno não encontrado.")


        


