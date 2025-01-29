import re

def filtrar_lista(lista_original, emojis_proibidos):
    regex_emoji = re.compile("|".join([re.escape(emoji) for emoji in emojis_proibidos]))
    return [linha for linha in lista_original if not regex_emoji.search(linha)]

def ler_lista_de_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"O arquivo {caminho_arquivo} não foi encontrado.")
        return []

def salvar_lista_em_arquivo(lista_filtrada, caminho_arquivo):
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            f.writelines([linha + '\n' for linha in lista_filtrada])
        print(f"Lista filtrada salva em {caminho_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

def exibir_estatisticas(lista_original, lista_filtrada):
    removidos = len(lista_original) - len(lista_filtrada)
    print(f"Linhas totais: {len(lista_original)}")
    print(f"Linhas removidas: {removidos}")
    print(f"Linhas restantes: {len(lista_filtrada)}")

def obter_lista():
    print("\nDigite ou cole sua lista de texto. Para finalizar, pressione ENTER duas vezes:")
    lista_original = []
    while True:
        linha = input()
        if linha == "":
            break
        lista_original.append(linha)
    return lista_original
