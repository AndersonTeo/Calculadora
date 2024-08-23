print("Bem-vindo à Calculadora Simples!\n")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\nEscolha a operação desejada:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = input("Digite o número da operação desejada (1/2/3/4): ")

if opcao == '1':
    resultado = num1 + num2
    operacao = "Soma"
elif opcao == '2':
    resultado = num1 - num2
    operacao = "Subtração"
elif opcao == '3':
    resultado = num1 * num2
    operacao = "Multiplicação"
elif opcao == '4':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Infinito (divisão por zero)"
    operacao = "Divisão"
else:
    print("Opção inválida. Encerrando o programa.")
    exit()

print(f"\nResultado da {operacao} com {num1} e {num2}:")
if isinstance(resultado, str):
    print(resultado)
else:
    print(f"Resultado: {resultado}")

print("\nGostaria de converter o resultado em inteiro? (s/n)")
resposta = input().lower()

if resposta == 's' and isinstance(resultado, (int, float)):
    resultado_int = int(resultado)
    print(f"\nResultado Convertido (int): {resultado_int}")
else:
    print("\nResultado mantido em float.")

