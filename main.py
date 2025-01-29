from banner import exibir_banner
from utils import (
    ler_lista_de_arquivo,
    salvar_lista_em_arquivo,
    filtrar_lista,
    exibir_estatisticas,
    obter_lista,
)
from args_handler import tratar_argumentos
import re

# Função para processar sinais
def processar_sinais(lista, timeframe):
    pattern = r"(\d{2}:\d{2})\s*([A-Z]{6})\s*(CALL|PUT)"
    resultados = []
    for linha in lista:
        match = re.search(pattern, linha)
        if match:
            time, pair, direction = match.groups()
            resultados.append(f"{time} {pair} {direction} {timeframe}")
    return resultados

# Função para exibir o menu
def exibir_menu():
    print("\nMenu de Opções:")
    print("1. Filtrar lista de texto (remover emojis proibidos)")
    print("2. Processar sinais com timeframes")
    print("0. Sair")
    return input("\nEscolha uma opção: ").strip()

# Função principal
def main():
    exibir_banner()  # Exibe o banner inicial
    print("Olá, seja bem-vindo!")

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            # Filtrar lista com emojis proibidos
            args = tratar_argumentos()
            if args.lista:
                lista_original = ler_lista_de_arquivo(args.lista)
            else:
                lista_original = obter_lista()

            emojis_proibidos = args.emojis if args.emojis else [
                "⛔️", "🚫", "❌️", "✖️", "⛔ ",
                "⛔️¹", "⛔️²", " ⛔️", "✖️²", "✖️¹", "✖️ ",
            ]

            lista_filtrada = filtrar_lista(lista_original, emojis_proibidos)
            exibir_estatisticas(lista_original, lista_filtrada)
            salvar_lista_em_arquivo(lista_filtrada, "lista_filtrada.txt")

            print("\nResultado: Lista filtrada")
            for linha in lista_filtrada:
                print(linha)

            print("\nFiltragem concluída!\n")

        elif opcao == "2":
            # Processar sinais
            lista_original = obter_lista()
            timeframe = input("\nEscolha o timeframe (M1 ou M5): ").strip()
            if timeframe not in ["M1", "M5"]:
                print("\nErro: O timeframe deve ser 'M1' ou 'M5'.")
            else:
                lista_processada = processar_sinais(lista_original, timeframe)
                salvar_lista_em_arquivo(lista_processada, "sinais_processados.txt")
                print("\nResultado: Lista processada")
                for linha in lista_processada:
                    print(linha)
                print("\nProcessamento concluído!\n")

        elif opcao == "0":
            print("\nSaindo do programa. Até mais!")
            break

        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
