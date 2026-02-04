def somar_horas_extras():
    numeros = []

    with open("hora_extra.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    for i in range(len(linhas)):
        linha = linhas[i].strip()

        if "dia de hora extra" in linha:
            numero = linhas[i + 1].strip()
            numeros.append(float(numero))

    calculo = (sum(numeros)) / 60
        
    print(f"{calculo:.2f}")
