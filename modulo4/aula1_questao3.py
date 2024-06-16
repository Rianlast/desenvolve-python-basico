# Leia n1, n2, n3
n1 = float(input("Informe n1: "))
n2 = float(input("Informe n2: "))
n3 = float(input("Informe n3: "))

# m = (n1 + n2 + n3) / 3
m = (n1 + n2 + n3) / 3

# Verifica as condições e imprime o resultado
if m >= 60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado")

# Imprima Fim
print("Fim")
