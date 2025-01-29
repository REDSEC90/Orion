import argparse

# Função para tratar argumentos da linha de comando
def tratar_argumentos():
    parser = argparse.ArgumentParser(description="Filtra uma lista de texto com emojis proibidos.")
    parser.add_argument("-l", "--lista", type=str, help="Caminho para o arquivo com a lista de texto", required=False)
    parser.add_argument("-e", "--emojis", type=str, nargs='+', help="Lista de emojis proibidos", required=False)
    args = parser.parse_args()
    return args
