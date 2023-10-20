import os

# id da cartela : números
cartelas = {
    '1309': [10, 6, 11, 13, 2, 25, 26, 28, 21, 17, 39, 41, 36, 34, 58, 51, 47, 55, 56, 66, 62, 70, 71, 73],
    '062': [12, 5, 3, 2, 4, 23, 26, 27, 28, 22, 40, 38, 32, 33, 52, 56, 57, 54, 60, 74, 67, 62, 61, 70],
    '428': [12, 15, 5, 11, 9, 23, 25, 28, 16, 19, 42, 34, 33, 44, 51, 53, 57, 48, 60, 71, 70, 66, 75, 74],
    '1404': [2, 14, 6, 5, 9, 21, 28, 17, 29, 19, 36, 42, 43, 31, 51, 47, 57, 54, 55, 66, 67, 73, 74, 62],
    '1306': [8, 11, 12, 3, 4, 27, 18, 19, 23, 26, 40, 44, 39, 34, 48, 49, 53, 56, 57, 64, 68, 71, 72, 63],
    '1308': [2, 10, 11, 12, 7, 26, 25, 27, 17, 22, 42, 35, 33, 34, 57, 47, 52, 55, 56, 62, 67, 70, 71, 72],
    '1401': [12, 7, 15, 6, 14, 24, 28, 27, 23, 22, 45, 40, 33, 39, 53, 57, 54, 46, 58, 68, 75, 62, 72, 70]
}

cartelas = dict(sorted(cartelas.items(), key=lambda item: int(item[0])))

# dicionário de backup para cada cartela
backup_cartelas = {nome: cartela.copy() for nome, cartela in cartelas.items()}

# quantidade de números faltantes
def imprimir_cartelas():
    os.system('clear')
    print()
    print('------------------------')
    print()
    print(f"Você possui {len(cartelas)} cartelas na base de dados!\n") # quantidade de cartelas na base
    
    for nome, cartela in cartelas.items():
        print(f"{nome}: {cartela}")
        print(f"FALTAM {len(cartelas[nome])} números")
        print()

# cartelas iniciais
imprimir_cartelas()

while True:
    entrada = input(
        "Digite um número (ou 'xd' para desfazer a última jogada): ")

    if entrada.lower() == 'xd':
        if not backup_cartelas:
            print("Nada para desfazer.")
        else:
            cartelas = {nome: cartela.copy()
                        for nome, cartela in backup_cartelas.items()}
            print("Desfez a última jogada.")
            imprimir_cartelas()
    else:
        try:
            numero = int(entrada)
            backup_cartelas = {nome: cartela.copy()
                               for nome, cartela in cartelas.items()}
            for nome, cartela in cartelas.items():
                if numero in cartela:
                    cartela.remove(numero)
            imprimir_cartelas()
        except ValueError:
            print("Por favor, insira um número válido.")
