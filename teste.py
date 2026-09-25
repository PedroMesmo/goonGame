def perguntar_opcao(pergunta, opcoes):
    while True:
        resposta = input(pergunta)

        if resposta in opcoes:
            return resposta

        print("Entrada inválida. Tente novamente.")

nome = input("Qual seu nome? ")

sexo = perguntar_opcao(
    "Digite M ou F: ",
    ["M", "F"]
)

tipo = perguntar_opcao(
    "Digite A, B ou C: ",
    ["A", "B", "C"]
)

print(nome, sexo, tipo)