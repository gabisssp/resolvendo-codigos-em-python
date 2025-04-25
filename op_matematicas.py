# Função para validar entrada numérica
def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

# Solicita os dois números ao usuário
numero1 = obter_numero("Digite o primeiro número: ")
numero2 = obter_numero("Digite o segundo número: ")

# Apresenta as opções de operação
print("\nEscolha a operação:")
print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

# Solicita a escolha da operação
while True:
    try:
        escolha = int(input("\nDigite o número da operação desejada (1-4): "))
        if 1 <= escolha <= 4:
            break
        else:
            print("Por favor, escolha uma opção entre 1 e 4.")
    except ValueError:
        print("Entrada inválida. Digite um número entre 1 e 4.")

# Realiza a operação escolhida
if escolha == 1:
    resultado = numero1 + numero2
    operacao = "+"
elif escolha == 2:
    resultado = numero1 - numero2
    operacao = "-"
elif escolha == 3:
    resultado = numero1 * numero2
    operacao = "*"
else:  # escolha == 4
    # Verificação de divisão por zero
    if numero2 == 0:
        print("\nErro: Divisão por zero não é permitida!")
        exit()
    resultado = numero1 / numero2
    operacao = "/"

# Exibe o resultado
print(f"\nResultado: {numero1} {operacao} {numero2} = {resultado}")