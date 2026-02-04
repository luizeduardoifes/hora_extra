with open("hora_extra.txt", "r", encoding="utf-8") as file:
    linhas = file.readlines()  # lê todas as linhas do arquivo

penultima_linha = linhas[-1].strip()  # pega a penúltima linha
primeiro_numero = penultima_linha[0]  # pega o primeiro caractere
print(primeiro_numero)
