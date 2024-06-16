#solicita ao usuário para inserir a avaliação do filme
avaliacao = int(input("Insira a avaliação do filme (1 a 5): "))

#classifica o filme com base na avaliação e imprime uma mensagem correspondente
if avaliacao == 5:
    print("Excelente!")
elif avaliacao == 4:
    print("Muito Bom!")
elif avaliacao == 3:
    print("Bom!")
elif avaliacao == 2:
    print("Regular.")
elif avaliacao == 1:
    print("Ruim.")
else:
    print("Avaliação inválida. Por favor, insira um número de 1 a 5.")

