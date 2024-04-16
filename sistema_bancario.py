import time

LIMITE_SAQUE = 3
LIMITE_POR_SAQUE = 500
saldo = valor = quantidade_saques = 0
extrato = ""

while True:
    print("""\n\n======= SISTEMA BANCÁRIO =======
            
[1] DEPÓSITO
[2] SAQUE
[3] EXTRATO
[0] SAIR      """)

    opcao = int(input("\n\nDigite a opção desejada: "))
    
    if opcao == 1:
        print("\n======== DEPÓSITO ========")
        valor = float(input("\nQuanto você deseja depositar? R$ "))
        if valor > 0:
            saldo += valor
            extrato += (f"Depósito: R$ {valor:.2f}\n")
        
        else:
            print("\nValor inválido! Tente novamente.")
        
    elif opcao == 2:
         print("\n======== SAQUE ========")
         
         if quantidade_saques == LIMITE_SAQUE:
             print("\nVocê atingiu o limite de 3 saques diários! Tente novamente amanhã.")
            
         
         elif saldo > valor:
            valor = float(input("\nQuanto você deseja sacar? R$ "))
            
            if valor > 0 and valor <= saldo:
                if valor <= LIMITE_POR_SAQUE:
                    saldo -= valor
                    quantidade_saques += 1
                    extrato += (f"Saque: R$ {valor:.2f}\n")
                else:
                    print("\nO valor máximo de saque permitido é de R$ 500,00! Tente novamente.")
            else:
                print("Valor inválido! Tente novamente.")
         
         elif saldo > 0 and valor == saldo:
            valor = float(input("\nQuanto você deseja sacar? R$ "))
            
            if valor > 0 and valor <= saldo:
                if valor <= LIMITE_POR_SAQUE:
                    saldo -= valor
                    quantidade_saques += 1
                    extrato += (f"Saque: R$ {valor:.2f}\n")
                else:
                    print("\nO valor máximo de saque permitido é de R$ 500,00! Tente novamente.")
            else:
                print("Valor inválido! Tente novamente.")
                
         else:
            print("\nVocê não tem dinheiro disponível para saque! Faça um depósito.")

    elif opcao == 3:
         print("\n======== EXTRATO ========")
         print(f"\n Seu saldo atual é de: R$ {saldo:.2f}")
         print(f"\n{extrato}")    
    elif opcao == 0:
         print("\nFinalizando programa...")
         time.sleep(1)
         break
    
    else:
         print("\nOpção inválida! Tente novamente.")

