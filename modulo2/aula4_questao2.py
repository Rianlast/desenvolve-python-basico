# leitura de dados (entrada)
Fahrenheit= int(input("digite a temperatura em F: "))

# processamento
celsius = (Fahrenheit - 32) * 5 / 9

#impressão de dados (saida)
print(f"{Fahrenheit} graus Fahrenheit são {int(celsius)} graus celsius. ")
