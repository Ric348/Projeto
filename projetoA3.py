
print('Você está ativo no ProjTrans.exe'.center(42))
print('-------------------------------------------- \nOlá, Boa noite!')
print()
print()
dadositem = []
while True:
    opcao = input('Adicionar produto (A) \nacesso ao estoque (B) \ncolocar produto em rota de transporte (C):\n').upper()
    print()
    print()
    if opcao == "A":
        while True:
            print('ADICIONAR PRODUTO:'.center(42))
            nomeproduto = input('Digite o nome do produto: ')
            nf = input('Digite a NF do produto: ')
            dadosrem = input('Digite o nome do remetente: ')
            dadosdest = input('Digite o nome do Destinatário: ')
            endereco = input('Digite o endereço do destinatário: EX:(Nome da rua, CEP, Ponto de referencia): ')
            print(f'O produto: {nomeproduto} da NF {nf} FOI SALVO NO SISTEMA !')
            print()
            dadositem.append((nomeproduto, nf))
            continuar = input('Deseja adicionar mais algum produto? (S/N) ?').upper()
            if continuar == "N":
                print("Saindo do programa......") 
                break
            elif continuar == "S":
                continue
    elif opcao == "B":
        if dadositem:
            for item in dadositem:
                print(f'Nome:{item[0]}, NF:{item[1]}')
        else:
            print('Nenhum produto adicionado!')                      
 