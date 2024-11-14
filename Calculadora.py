# Calculadora Simples: lê dois números e um operador aritmético e realiza a operação correspondente.
(+, -, *, /) e realize a operação correspondente.

# Criação da função calcular()
def Calcular():
    
    while True: #Criação de umloop contínuo já que não sei quando serão inseridas entradas válidas.
        try: # Abertura do Gerenciamento de erros com try-except
            #inputs para usuário inserir entradas a serem usadas posteriormente (números já convertidos em ponto flutuante).
            numero1 = float(input("Digite o primeiro número: ")) 
            numero2 = float(input("Digite o segundo número"))
            operador = input("Digite o operador (+, -, *, /): ")
            # Utilização de match-case (escolha caso), funcionalidade presente no Python a partir da versão 3.10.
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

# Chamando a função criada:
Calcular()
