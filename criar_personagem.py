from gooner import Goon

def criar_personagem():

    def questao(pergunta, opcoes):
        while True:
            resposta = input(pergunta)

            if resposta in opcoes:
                return resposta

            print("Comando descabível")

    gooner = Goon(0,0,0,0,0,0,0,0,0)

    mulher = questao('Mulher(trans, btw)\n[S]Sim    [N]Não')
    if mulher == 's':
        gooner.mulher = True
    else:
        gooner.mulher = False

    femboy = questao('Femboy\n[S]Sim    [N]Não', ['s','n'])
    if femboy == 's':
        gooner.femboy = True
    else:
        gooner.femboy = False

    furry = questao('Furry\n[S]Sim     [N]Não\n',['s','n'])
    if furry == 's':
        gooner.furry = True
    else:
        gooner.furry = False



    gooner.exibir_status()
        
criar_personagem()
