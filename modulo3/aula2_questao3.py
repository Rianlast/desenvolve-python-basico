#pergunta a idade do usuario
idade = int(input("Qual é a sua idade? "))

#pergunta se ja jogou pelo menos 3 jogos de tabuleiro
jogou_jogos = input("Você já jogou pelo menos 3 jogos de tabuleiro? (True/False) ")
jogou_jogos = jogou_jogos == 'True'


#pergunta quantas vezes venceu um jogo
vitorias = int(input("Quantas vezes você venceu um jogo? "))


#verificação para admissão no clube
admissao = (16 <= idade <= 18) and jogou_jogos and (vitorias >= 1)

#resultado da verificação
print(admissao)



