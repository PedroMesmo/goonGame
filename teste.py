from gooner import Goon

def criar_personagem():

    # Função para permitir somente respostas válidas perante a suprema corte
    def questao(pergunta, opcoes):
        while True:
            resposta = input(pergunta).lower()

            if resposta in opcoes:
                return resposta

            print("Comando descabível")

    gooner = Goon(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    # Definindo o gênero
    mulher = questao(
        'Mulher(trans, btw)\n[S]Sim    [N]Não\n',
        ['s', 'n']
    )

    if mulher == 's':
        gooner.mulher = True
    else:
        gooner.mulher = False

    # Definindo a religião
    religiao = questao(
        'Religião\n'
        '[1] Cristianismo\n'
        '[2] Judaísmo\n'
        '[3] Islamismo\n'
        '[4] Budismo\n'
        '[5] Satanismo\n'
        '[6] Lei Felca\n'
        '[7] Outro\n',
        ['1', '2', '3', '4', '5', '6', '7']
    )

    if religiao == '1':
        gooner.religiao = 'cristianismo'
    elif religiao == '2':
        gooner.religiao = 'judaismo'
    elif religiao == '3':
        gooner.religiao = 'islamismo'
    elif religiao == '4':
        gooner.religiao = 'budismo'
    elif religiao == '5':
        gooner.religiao = 'satanismo'
    elif religiao == '6':
        gooner.religiao = 'Lei Felca'
    else:
        gooner.religiao = input(
            'Certo diferentão, nos conte qual a sua religião ultra nichada: '
        )

    # Femboy
    femboy = questao(
        'Femboy\n[S]Sim    [N]Não\n',
        ['s', 'n']
    )
    gooner.femboy = femboy == 's'

    # Furry
    furry = questao(
        'Furry\n[S]Sim    [N]Não\n',
        ['s', 'n']
    )
    gooner.furry = furry == 's'

    gooner.exibir_status()


criar_personagem()
