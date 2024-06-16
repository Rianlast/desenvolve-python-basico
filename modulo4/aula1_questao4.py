# Leia n
n = int(input("Digite o valor de n: "))
maior = 0

# Enquanto n for maior que 0
while n > 0:
    # Leia x
    x = int(input("Digite um numero: "))
    
    # Se x for maior que maior, atualize maior
    if x > maior:
        maior = x
    
    # Decrementa n
    n -= 1

# Imprima o maior numero lido
print("O maior numero é:", maior)
