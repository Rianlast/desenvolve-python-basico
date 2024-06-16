#solicita ao usuário para inserir a distância e o peso do pacote
distancia = float(input("Insira a distância da entrega em quilômetros: "))
peso = float(input("Insira o peso do pacote em quilogramas: "))

#calcula o valor do frete com base na distância
if distancia <= 100:
    frete = peso * 1
elif distancia <= 300:
    frete = peso * 1.5
else:
    frete = peso * 2

#acrescenta uma taxa para pacotes com peso superior a 10 kg
if peso > 10:
    frete += 10

print(f"O valor do frete é: R${frete:.2f}")
















