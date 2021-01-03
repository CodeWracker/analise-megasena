from service import *

functions = [
    apiFetch,
    analiseLocal,
    verificaAcertos
]

def inicio():
    print("----------------------------------------------------------------")

    print("Selecione o que quer fazer:")
    print("0 - Baixar e analisar os dados do jogo X ao Y")
    print("1 - Analisar os dados ja baixados")
    print("2 - Verificar, do jogo X ao Y, caso tenha jogado, o que ganharia")

    print("----------------------------------------------------------------")

    escolha = int(input("Digite sua escolha: "))
    functions[escolha]()

inicio()
