from datetime import datetime

# Obtém a data e hora atuais
agora = datetime.now()

# Formata os atributos de data e hora para garantir que tenham dois dígitos
# Adiciona um zero à esquerda se o dia ou mês for menor que 10
dia = f"{agora.day:02d}"
mes = f"{agora.month:02d}"
ano = f"{agora.year}"
hora = f"{agora.hour:02d}"
minuto = f"{agora.minute:02d}"

# Monta a string de data e hora no formato desejado
data_formatada = f"Data: {dia}/{mes}/{ano}\nHora: {hora}:{minuto}"

# Exibe a data e hora formatadas
print(data_formatada)
