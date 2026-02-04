import os
from services.calc_hora import para_minutos
from services.ler_hora_extra import somar_horas_extras

from services.numeros_dias import numero_dia

lista = []
dias = numero_dia()


while True:
    os.system("cls")
    dias += 1
    lista.append(dias)
    
    print("escolhe o expediente:\n1: meio de semana\n2: fim de semana")
    opcao1 = int(input(""))
    
    os.system("cls")
    print(f"{dias} dia de expediente")
    if opcao1 == 1:
        entrada = input("digite a hora da entrada: ")
        inicio_intervalo = input("digite o horario do intervalo: ")
        fim_intervalo = input("digite o horario retornando do serviço pós intervalo: ")
        saida = input("digite a hora da saida: ")

        entrada_m = para_minutos(entrada)
        inicio_int_m = para_minutos(inicio_intervalo)
        fim_int_m = para_minutos(fim_intervalo)
        saida_m = para_minutos(saida)

        tempo_total = saida_m - entrada_m
        intervalo = fim_int_m - inicio_int_m
        tempo_trabalhado = tempo_total - intervalo
        hora_extra = tempo_trabalhado - 495
    
    elif opcao1 == 2:
        entrada = input("digite a hora da entrada: ")
        saida = input("digite a hora da saida: ")
        
        entrada_m = para_minutos(entrada)
        saida_m = para_minutos(saida)
        tempo_trabalhado = saida_m - entrada_m
        hora_extra = tempo_trabalhado - 270
    
    with open("hora_extra.txt", "a+", encoding="utf-8") as file:
        
        file.write(f"{dias} dia de hora extra\n")
        file.write(f"{hora_extra}\n\n")
        print("arquivo salvo com sucesso")
        
    with open("dias.txt","a+") as file:
        file.write(",".join(map(str, lista)))
    
    opcao2 = input("deseja continuar o sistema? ")
    if opcao2 == "sim":
        continue

    if opcao2 == "nao":
        print(f"as horas extras que você tem ao todo é de: {somar_horas_extras()}")
        break
        


        
    


