import random

# Gera um número aleatório entre 1 e 10
numero_aleatorio = random.randint(1, 10)

# Inicializa a variável de palpite do usuário
palpite_usuario = 0

# Loop que continua até o usuário acertar o número
while palpite_usuario != numero_aleatorio:
    # Pede ao usuário para adivinhar o número
    palpite_usuario = int(input("Adivinhe o número entre 1 e 10: "))
    
    # Fornece feedback sobre o palpite
    if palpite_usuario > numero_aleatorio:
        print("Muito alto, tente novamente!")
    elif palpite_usuario < numero_aleatorio:
        print("Muito baixo, tente novamente!")

# Informa ao usuário que ele acertou
print(f"Correto! O número é {numero_aleatorio}.")
