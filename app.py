import os
restaurantes=[{"nome":"cantinho do sabor","categoria":"sabor","ativo":True},
              {"nome":"tesouro da mesa","categoria":"mesa","ativo":True},
              {"nome":"ponto chic","categoria":"chic","ativo":False}
            ]
def exibir_nome_do_programa():
    print("cantinho do sabor")

def exibir_opções():
    print('1- Cadastrar restaurante')
    print('2- Listar restaurante')
    print('3- Ativar restaurante')
    print('4- Sair\n')

def Encerrando_programa():
    exibir_subtitulo("encerrando o programa")
    os.system('cls')
    print('Encerrando o programa')
    

def cadastrar_novo_restaurantes():
    exibir_subtitulo("cadastra de novo restaurante")
    nome_do_restaurante=input("digite o nome do restaurante que deseja cadastra")
    restaurantes.append(nome_do_restaurante)
    print(f"o restaurante{nome_do_restaurante}foi cadastrado com sucesso!")
    voltar_ao_menu_principal()
    
def opcao_invalida():
    print('Opção Inválida!\n')
    main()
    
def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal")
    main()
    
def exibir_subtitulo(texto):
    os.system("cls")
    print(texto)
    print()

def listar_restaurante():   
    exibir_subtitulo("listando restaurante") 
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        print(f"-{nome_restaurante}")
        voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida= int(input('Escolha uma opção: '))
        print (f'Você escolheu a opção: {opcao_escolhida}\n')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurantes()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            print('Ativar restaurantes')
        elif opcao_escolhida == 4:
            Encerrando_programa()
        else:
            opcao_invalida()
    except:
         opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opções()
    escolher_opcao()

if __name__ == '__main__':
    main()


    