from service import *
from estimator import *

functions = [
    apiFetch,
    analiseLocal,
    verificaAcertos,
    verificaCombinacoes
]

def inicio():
    print("----------------------------------------------------------------")

    print("Selecione o que quer fazer:")
    print("0 - Baixar e analisar os dados do jogo X ao Y")
    print("1 - Analisar os dados ja baixados")
    print("2 - Verificar, do jogo X ao Y, caso tenha jogado, o que ganharia")
    print("3 - Verificar as combinacoes existentes em um arquivo local")

    print("----------------------------------------------------------------")

    escolha = int(input("Digite sua escolha: "))
    functions[escolha]()

inicio()
