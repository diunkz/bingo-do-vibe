# Crie um dicionário onde as chaves são os nomes das cartelas e os valores são as listas de números
cartelas = {
    'id1': [7, 19, 33, 50, 66, 2, 15, 35, 54, 72, 10, 23, 40, 59, 76, 1, 16, 29, 47, 65, 11, 22, 37, 53],
    'id2': [12, 27, 36, 49, 68, 6, 18, 38, 52, 75, 8, 25, 34, 45, 63, 9, 21, 39, 51, 70, 5, 20, 30, 48],
    'id3': [13, 24, 31, 46, 60, 4, 14, 32, 57, 71, 3, 17, 41, 56, 69, 7, 26, 44, 55, 73, 15, 28, 42, 62],
    'id4': [1, 16, 30, 45, 64, 2, 19, 33, 50, 70, 8, 22, 34, 52, 75, 9, 25, 35, 47, 67, 11, 23, 38, 53],
    'id5': [14, 27, 31, 49, 68, 7, 15, 32, 59, 71, 10, 20, 36, 55, 66, 6, 18, 40, 57, 73, 3, 12, 37, 54]
}

# Crie um dicionário de backup para cada cartela
backup_cartelas = {nome: cartela.copy() for nome, cartela in cartelas.items()}

# Função para imprimir as cartelas e a quantidade de números faltantes
def imprimir_cartelas():
    for nome, cartela in cartelas.items():
        print(f"{nome}: {cartela}")
        print(f"FALTAM {len(cartelas[nome])} números")
        print()

# Imprime as cartelas iniciais
imprimir_cartelas()

while True:
    entrada = input("Digite um número (ou 'xd' para desfazer a última jogada): ")
    
    if entrada.lower() == 'xd':
        if not backup_cartelas:
            print("Nada para desfazer.")
        else:
            cartelas = {nome: cartela.copy() for nome, cartela in backup_cartelas.items()}
            print("Desfez a última jogada.")
            imprimir_cartelas()
    else:
        try:
            numero = int(entrada)
            backup_cartelas = {nome: cartela.copy() for nome, cartela in cartelas.items()}
            for nome, cartela in cartelas.items():
                if numero in cartela:
                    cartela.remove(numero)
            imprimir_cartelas()
        except ValueError:
            print("Por favor, insira um número válido.")
