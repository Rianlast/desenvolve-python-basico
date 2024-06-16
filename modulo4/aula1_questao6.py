# Leia o número de testes
N = int(input("Digite o número de testes: "))
total_cobaias = 0
total_coelhos = 0
total_ratos = 0
total_sapos = 0

# Leia a quantidade e o tipo de cobaia para cada teste
for _ in range(N):
    dados = input("Digite a quantidade e o tipo de cobaia (ex: 5 C): ").split()
    quantidade = int(dados[0])
    tipo = dados[1]
    
    # Acumule o total de cobaias e o total por tipo
    total_cobaias += quantidade
    if tipo == 'C':
        total_coelhos += quantidade
    elif tipo == 'R':
        total_ratos += quantidade
    elif tipo == 'S':
        total_sapos += quantidade

# Calcule os percentuais
percentual_coelhos = (total_coelhos / total_cobaias) * 100
percentual_ratos = (total_ratos / total_cobaias) * 100
percentual_sapos = (total_sapos / total_cobaias) * 100

# Imprima os resultados
print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")
