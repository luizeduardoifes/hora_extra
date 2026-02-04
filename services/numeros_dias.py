import os



def numero_dia():
    os.system("cls")
    print("1-criar nova lista de horas extras\n2-continuar com a mesma lista de horas extras")
    opcao = int(input("Escolha uma opção: "))
    match opcao:
        case 1:
            with open("hora_extra.txt", "w"):
                pass
            
            with open("dias.txt", "w"):
                pass
            
            return 0
            
            
        case 2:
            if not os.path.exists("dias.txt"):
                return 0

            with open("dias.txt", "r", encoding="utf-8") as file:
                conteudo = file.read().strip()

            if not conteudo:
                return 0

            partes = [p for p in conteudo.split(",") if p.strip() != ""]
            if not partes:
                return 0

            try:
                return int(partes[-1])
            except ValueError:
                return 0
            
