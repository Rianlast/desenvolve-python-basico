#solicita a classe de personagem escolhida
classe = input("Qual é a classe do personagem? (guerreiro, mago ou arqueiro) ")

#solicita os pontos de força e magia atribuídos ao personagem
forca = int(input("Quantos pontos de força foram atribuídos ao personagem? "))
magia = int(input("Quantos pontos de magia foram atribuídos ao personagem? "))

#verifica se os pontos de atributo são consistentes com a classe escolhida
if classe == 'guerreiro':
    validacao = forca >= 15 and magia <= 10
elif classe == 'mago':
    validacao = forca <= 10 and magia >= 15
elif classe == 'arqueiro':
    validacao = 5 < forca <= 15 and 5 < magia <= 15
else:
    validacao = False

#resultado da validação
print(validacao)
