print("Bem vindo ao simulador de controle de veículo da empresa AutoDrive")
velocidade_do_carro = 0 
carro_ligado = False
marcha_atual = 0 
faixas_marcha = [(0, 0), (0, 20), (20, 40), (40, 60), (60, 80), (80, 100), (100, 120)]

def verificar_carro_ligado():
    if not carro_ligado:
        print("O carro precisa estar ligado.")
        return False
    return True

def ligar_carro():
    global carro_ligado
    if not carro_ligado:
        print("Carro ligado.")
        carro_ligado = True
    else:
        print("Carro já está ligado.")

def desligar_carro():
    global carro_ligado
    global velocidade_do_carro
    global marcha_atual
    if not carro_ligado:
        print("Carro já está desligado.")
    elif velocidade_do_carro > 0:
        print("Reduza a velocidade para 0 km/h para desligar o carro.")
    elif marcha_atual != 0:
        print("Coloque a marcha em ponto morto (0) para poder desligar o carro.")
    else:    
        print("Carro desligado.")
        carro_ligado = False

def acelerar_carro():
    global velocidade_do_carro
    global marcha_atual
    if not verificar_carro_ligado():
        return
    if marcha_atual == 0:
        print("O carro está em ponto morto. Mude para a primeira marcha para acelerar.")
    else:
        faixa = faixas_marcha[marcha_atual]
        velocidade_maxima = faixa[1]
        if velocidade_do_carro < velocidade_maxima:
            velocidade_do_carro += 1
            print(f"Velocidade: {velocidade_do_carro} km/h")
        else:
            print("Velocidade máxima permitida para essa marcha.")

def diminuir_velocidade_do_carro():
    global velocidade_do_carro
    global marcha_atual
    if not verificar_carro_ligado():
        return
    if velocidade_do_carro > 0:
        nova_velocidade = velocidade_do_carro - 1
        velocidade_minima = faixas_marcha[marcha_atual][0]
        if nova_velocidade < velocidade_minima:
            print(f"Não é possível reduzir para {nova_velocidade} km/h na marcha {marcha_atual}.")
            print(f"Velocidade mínima da marcha atual: {velocidade_minima} km/h")
        else:
            velocidade_do_carro = nova_velocidade
            print(f"Velocidade: {velocidade_do_carro} km/h")
    else:
        print("O carro já está parado.")

def mudar_direcao_do_carro():
    if not verificar_carro_ligado():
        return
    if 1 <= velocidade_do_carro and velocidade_do_carro <= 40:
        while True:
            direcao_do_carro = input("Digite 'esquerda' ou 'direita': ").lower()
            if direcao_do_carro in ['esquerda', 'direita']:
                print(f"Direção virada para: {direcao_do_carro}")
                break  
            else:
                print("Direção inválida, digite novamente.")
    else:
        print("A velocidade precisa estar entre 1 e 40 km/h para mudar de direção.")

def mudar_marcha_do_carro():
    global velocidade_do_carro
    global marcha_atual
    if not verificar_carro_ligado():
        return
    while True:
        marcha = input("Digite a marcha desejada (0 a 6): ")
        if not marcha.isdigit():
            print("Entrada inválida, digite um número.")
            continue

        nova_marcha = int(marcha)
        if nova_marcha < 0 or nova_marcha > 6:
            print("Marcha inválida. Digite um valor entre 0 e 6.")
            continue
        if nova_marcha == marcha_atual:
            print("O carro já está nessa marcha.")
            continue
        elif nova_marcha > marcha_atual + 1 or nova_marcha < marcha_atual - 1:
            print("Só é possível mudar uma marcha por vez.")
            continue
        faixa = faixas_marcha[nova_marcha]
        if velocidade_do_carro < faixa[0] or velocidade_do_carro > faixa[1]:
            print(f"Velocidade atual incompatível com a marcha {nova_marcha}.")
            print(f"Para passar para a marcha {nova_marcha}, a velocidade deve estar entre {faixa[0]} e {faixa[1]} km/h.")
            print("Ajuste a velocidade primeiro antes de tentar mudar de marcha.")
            return 
        print(f"Marcha alterada para {nova_marcha}.")
        marcha_atual = nova_marcha
        break

def estado_do_carro():
    if carro_ligado:
        estado = "Sim"
    else:
        estado = "Não"
    print(f"Carro ligado: {estado}")
    print(f"Velocidade: {velocidade_do_carro} km/h")
    print(f"Marcha atual: {marcha_atual}")

while True:
    print("========== Menu ============")
    print("1 - Ligar o carro")
    print("2 - Acelerar")
    print("3 - Diminuir velocidade")
    print("4 - Mudar direção")
    print("5 - Desligar o carro")
    print("6 - Mudar marcha")
    print("7 - Mostrar estado atual")
    print("8 - Sair")
    print("===========================")

    opcao = input("Opção: ")
    match opcao:
        case "1":
            ligar_carro()
        case "2":
            acelerar_carro()
        case "3":
            diminuir_velocidade_do_carro()
        case "4":
            mudar_direcao_do_carro()
        case "5":
            desligar_carro()
        case "6":
            mudar_marcha_do_carro()
        case "7":
            estado_do_carro()
        case "8":
            if carro_ligado:
                print("Desligue o carro antes de sair do simulador.")
                continue
            print("Saindo do simulador...")
            break
        case _:
            print("Opção inválida.")

