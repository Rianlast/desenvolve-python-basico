# Leia a quantidade de respondentes
N = int(input("Digite a quantidade de respondentes: "))
soma_idades = 0

# Leia as idades dos respondentes
for i in range(N):
    idade = int(input(f"Digite a idade do respondente {i+1}: "))
    soma_idades += idade

# Calcule e imprima a média das idades
media_idades = soma_idades / N
print("A média das idades é:", media_idades)
