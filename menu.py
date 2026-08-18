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

elif calculo == 3:
    print("Você escolheu multiplicar.")
    resultado = calculadora.multiplicar(a, b)
    print('O resultado da multiplicação é:', resultado)

elif calculo == 4:
    print("Você escolheu dividir.")
    resultado = calculadora.dividir(a, b)
    print('O resultado da divisão é:', resultado)