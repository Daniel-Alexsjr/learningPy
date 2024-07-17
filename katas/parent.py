texto = "aabbcdd"

for i in range(len(texto) - 1):
    if texto[i] == texto[i + 1]:
        print(f"O caractere '{texto[i]}' é igual ao próximo caractere.")