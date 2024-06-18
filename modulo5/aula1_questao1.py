# Solicita ao usuário que insira dois números decimais
primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

# Calcula a diferença absoluta entre os dois números
diferenca_absoluta = abs(primeiro_numero - segundo_numero)

# Arredonda o resultado para duas casas decimais
resultado_arredondado = round(diferenca_absoluta, 2)

# Exibe o resultado
print(f"A diferença absoluta entre os números é: {resultado_arredondado}")
