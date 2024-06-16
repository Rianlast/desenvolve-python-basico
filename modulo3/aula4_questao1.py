#solicita os dois numeros
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

#calcula a soma dos dois numeros
soma = numero1 + numero2

#verifica se a soma e par ou impar e imprime o resultado
if soma % 2 == 0:
    print("A soma e par.")
else:
    print("A soma e impar.")
