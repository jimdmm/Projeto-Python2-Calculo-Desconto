def menu():
    tela = """
    Opção de desconto:     
        1 - 10% de desconto
        2 - 20% de desconto
        3 - 30% de desconto
        4 - 80% de desconto
        0 ou q - Sair
    """
    print(tela)


def calcula(valor, desconto):
    return valor * desconto
    
def valor(valor, desconto_aplicado):
    return valor - desconto_aplicado
    
def resultado(valor, desconto_aplicado, valor_desconto):
    result = f"""
    ======================================
    ======================================
    Valor original:    R$ {valor:.2f}
    Desconto aplicado: R$ {desconto_aplicado:.2f}
    Valor com desconto: R$ {valor_desconto:.2f}
    ======================================
    ======================================
    """
    print(result)
    
parada = 0
desconto = 0

while parada == 0:
    menu()
    
    opcao = input("Escolha uma opção: ")
    
    if opcao not in ("1", "2", "3", "4", "0", "q"):
        print("Opção inválida, tente novamente!")
        
    elif opcao == '0' or opcao.lower() == 'q':
        print("Obrigado por usar o programa")
        break
        
    else:
        valorTotal = float(input("Informe o valor da compra: "))
        
        if opcao == "1":
            desconto = 0.1
        elif opcao == "2":
            desconto = 0.2
        elif opcao == "3":
            desconto = 0.3
        elif opcao == "4":
            desconto = 0.8
            
        desconto_aplicado = calcula(valorTotal, desconto)
        valor_desconto = valor(valorTotal, desconto_aplicado)
        resultado(valorTotal, desconto_aplicado, valor_desconto)
