# Solicita a string e o número ao usuário
texto = input("Digite uma string: ")

# Verifica se o número inserido é realmente um inteiro
while True:
    try:
        numero = int(input("Digite quantas vezes a string deve ser repetida: "))
        if numero >= 0:  # Verifica se o número é não-negativo
            break
        else:
            print("Por favor, digite um número não-negativo.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

# Repete a string o número de vezes informado
#resultado = texto * numero

# Cria uma string com quebras de linha
resultado = (texto + "\n") * numero

# Exibe o resultado
print("\nResultado:")
print(resultado)

