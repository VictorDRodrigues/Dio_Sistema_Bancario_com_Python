menu = """

    Opções
-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-    
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-
=> """

saldo = 0
limite = 500
extrato = ''
numero_saque = 0
LIMITE_SAQUE = 3
linha = str('-='*11 + '=-'*11)

while True:

    opcao = input(menu)

    if opcao == 'd':
        print('Deposito')
        valordeposito = float(input('Digite o valor do DEPOSITO. R$ '))
        if valordeposito <= 0:
            print(linha)
            print(f'O valor R${valordeposito:.2f} é ZERO ou NEGATIVO,\n seu deposito não é VALIDO!')
            print(linha)

        else:
            saldo += valordeposito
            print(linha)
            print(f'Seu novo Saldo é de R${saldo:.2f}')
            print('Desejamos a você um bom dia, volte sempre.')
            print(linha)

    elif opcao == 's':
        print('Saque')
        if numero_saque == LIMITE_SAQUE:
            print('Infelizmente já foi realizado os 3 SAQUES diários.\nCaso ainda deseje sacar, vá a uma agência mais próxima de você. ')

        else:
            valorsaque = float(input('Digite o valor do SAQUE. R$ '))

            if valorsaque <= 0:
                print(linha)
                print(f'O valor R${valorsaque:.2f} é ZERO ou NEGATIVO,\n seu SAQUE não é VALIDO!')
                print(linha)

            if valorsaque > 500:
                print(linha)
                print(f'O valor R${valorsaque:.2f} é maior que o LIMITE de SAQUE,\n seu LIMITE de SAQUE é R$ {limite}')
                print(linha)

            if valorsaque > saldo:
                print(linha)
                print(f'O valor R${valorsaque:.2f} é maior que o LIMITE de SALDO,\n seu LIMITE de SAQUE é R$ {saldo}')
                print(linha)

            else:
                saldo -= valorsaque
                numero_saque += 1
                print(linha)
                print(f'Seu novo Saldo é de R${saldo:.2f}')
                print('Desejamos a você um bom dia, volte sempre.')
                print(linha)

    elif opcao == 'e':
        print(linha)
        print('Extrato')
        print(f'Seu Saldo é de R${saldo:.2f} !')
        print('Desejamos a você um bom dia, volte sempre.')
        print(linha)

    elif opcao == 'q':
        break

    else:
        print('Operação INVÁLIDA, por favor selecione novamente a operação desejada.')
