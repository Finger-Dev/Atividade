# Calculadora Simples: lê dois números e um operador aritmético e realiza a operação correspondente.
(+, -, *, /) e realize a operação correspondente.

def calcular():
    while True: #loop contínuo já que não sei quando serão inseridas entradas válidas.
        try:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número"))
            operador = input("Digite o operador (+, -, *, /): ")

            match operador:
                case '+':
                    resultado = numero1 + numero2
                case '-':
                    resultado = numero1 - numero2
                case '*':
                    resultado = numero1 * numero2
                case '/':
                    if numero2 != 0:
                        resultado = numero1 / numero2
                    else:
                        print ("Divisão por zero não é aceita")
                        continue # Volta ao início do loop
                case _: 
                    print ("Escolha um operador válido.")
                    continue # Volta ao início do loop

            # Em não havendo erros, exibe o resultado:
            print(f"O resultado de {numero1} {operador} {numero2} é: {resultado}")   
            break # Para sair do loop!

        except ValueError: # exceção ao Try
            print("Insira números válidos.")

calcular()
