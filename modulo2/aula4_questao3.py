#Inicialização das variáveis para armazenar a soma total (entrada)
total = 0

#Loop para obter informações dos produtos e calcular o preço total
for i in range(1, 4):

#Entrada de dados do usuário



 print(f'Digite o nome do produto {i}: ', end='')
nome = input()

print(f'Digite o preço unitário do produto {i}: R$', end='')
preco_unitario = float(input())

print(f'Digite a quantidade do produto {i}: ', end='')
quantidade = int(input())

#Cálculo do preço total para o produto atual
total += preco_unitario * quantidade

#Formatação do preço total com duas casas decimais e separador de milhar
total_formatado = f'Total: R${total:,.2f}'.replace(',', '.')

#saida de dados
print(total_formatado)
