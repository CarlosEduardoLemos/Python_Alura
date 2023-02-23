import forca
import adivinhação

def escolhe_jogo():

    print("*****************************")
    print("**** Escolhe o seu Jogo! ****")
    print("*****************************")

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("\nQual Jogo?"))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando divinhação")
        adivinhação.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()