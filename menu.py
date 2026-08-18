import calculadora
def menu():
    print("Escolha uma operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sair")

    calculo = int(input("Digite o número da operação desejada: "))
    return calculo

calculo = menu()
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if calculo == 1:
    print("Você escolheu somar.")
    resultado = calculadora.somar(a, b)
    print('O resultado da soma é:', resultado)

elif calculo == 2:
    print("Você escolheu subtrair.")
    resultado = calculadora.subtrair(a, b)
    print('O resultado da subtração é:', resultado)