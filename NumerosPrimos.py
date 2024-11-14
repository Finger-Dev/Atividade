# Números Primos de 1 a *N*, este inserido pelo usuário.

# Enquanto tiver valor True (enquanto for reconhecido como verdadeiro):
while True:
    # Controle e gerenciamento de erros via try-except:
    try:
        num = int(input("Digite um número inteiro: ")) # Já pede número "inteiro" via int()
        # Se entrada for menor que 2, o número será reconhecido como inválido e o programa retorna pedidndo um número aceitável:
        if num < 2:
            print("Favor digitar um número válido (maior ou igual a 2): ")
            continue # recomeça o loop para solicitar um número
        
        primos = []  # lista para armazenar os números primos

        # Loop 'for' verifica números de 2 até 'num':
        for numero in range(2, num + 1):
            primo = True #Supõe que o número seja primo.

            # Verifica se 'numero' é divisível por qualquer número de 2 até a raiz quadrada de 'numero'.
            for i in range(2, int(numero ** 0.5) + 1):
                if numero % i == 0: # sendo divisível, não é primo.
                    primo = False
                    break # Para sair do loop interno
            
            # Considerados primos, serão incluídos na lista [] através da função do python, append()
            if primo:
                primos.append(numero)

        print(f"Números primos entre 1 e {num}: {primos}")
        break  # Sai do loop após operação bem-sucedida

    except ValueError: # Controle e gerenciamento de erros: captura entrada inválida.
        print("Entrada inválida. Favor inserir número válido.")


