import random
import math

# Pede ao usuário para inserir o valor de n
n = int(input("Digite o valor de n: "))

# Gera n valores inteiros aleatórios entre 0 e 100 e calcula a soma
soma = sum(random.randint(0, 100) for _ in range(n))

# Calcula a raiz quadrada da soma dos valores
raiz_quadrada = math.sqrt(soma)

# Exibe o resultado
print(f"A raíz quadrada da soma dos valores é: {raiz_quadrada}")
