from Utils.cadastrar import cadastrar
from Utils.editar import editar
from Utils.delete import delete
from Utils.read import read
import os


# While true para manter o programa rodando
while True:
    # Menu
    print('----------------------------------')
    print('1 - Cadastrar vendedor')
    print('2 - Update vendedor')
    print('3 - Ver Vendedores')
    print('4 - Deletar vendedor')
    print('----------------------------------')
    print('5 - Cadastrar cliente')
    print('6 - Update cliente')
    print('7 - Ver clientes')
    print('8 - Deletar cliente')
    print('----------------------------------')
    print('9 - Cadastrar produto')
    print('10 - Update produto')
    print('11 - Ver produtos')
    print('12 - Deletar produto')
    print('----------------------------------')
    print('13 - Cadastrar Favorito')
    print('14 - Delete Favorito')
    print('15 - Ver Favoritos')
    print('----------------------------------')
    print('16 - Cadastrar compra')
    print('17 - Delete compra')
    print('18 - Ver compras')
    print('----------------------------------')
    print('S - Sair')
    # Recebendo a opção
    opcao = input('Opção: ')
    # Verificando a opção
    if (opcao == 1 or opcao == '1'):
        cadastrar('vendedor')
        os.system('cls')
    elif (opcao == 2 or opcao == '2'):
        editar('vendedor')
        os.system('cls')
    elif (opcao == 3 or opcao == '3'):
        read('vendedor')
        os.system('cls')
    elif (opcao == 4 or opcao == '4'):
        delete('vendedor')
        os.system('cls')
    elif (opcao == 5 or opcao == '5'):
        cadastrar('cliente')
        os.system('cls')
    elif (opcao == 6 or opcao == '6'):
        editar('cliente')
        os.system('cls')
    elif (opcao == 7 or opcao == '7'):
        read('cliente')
        os.system('cls')
    elif (opcao == 8 or opcao == '8'):
        delete('cliente')
        os.system('cls')
    elif (opcao == 9 or opcao == '9'):
        cadastrar('produto')
        os.system('cls')
    elif (opcao == 10 or opcao == '10'):
        editar('produto')
        os.system('cls')
    elif (opcao == 11 or opcao == '11'):
        read('produto')
        os.system('cls')
    elif (opcao == 12 or opcao == '12'):
        delete('produto')
        os.system('cls')
    elif (opcao == 13 or opcao == '13'):
        cadastrar('favorito')
        os.system('cls')
    elif (opcao == 14 or opcao == '14'):
        delete('favorito')
        os.system('cls')
    elif (opcao == 15 or opcao == '15'):
        read('favorito')
        os.system('cls')
    elif (opcao == 16 or opcao == '16'):
        cadastrar('compra')
        os.system('cls')
    elif (opcao == 17 or opcao == '17'):
        delete('compra')
        os.system('cls')
    elif (opcao == 18 or opcao == '18'):
        read('compra')
        os.system('cls')
    elif (opcao == 'S' or opcao == 's'):
        break
    else:
        print('Opção inválida!')
        
