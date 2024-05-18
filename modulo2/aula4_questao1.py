# leitura de dados (entrada)
comprimento = int(input("digite o comprimento:"))
largura     = int(input("digite a largura:"))
preço_m2    = float(input("valor do m2:"))

# processamento
area = comprimento * largura #m2
preço_total = area * preço_m2

#impressão de dados (saida)
print(f"o terreno possui {area}m2 e custa R${preço_total:,.2}")
