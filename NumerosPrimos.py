# Números Primos de 1 a *N*, este inserido pelo usuário.

while True:
    try:
        num = int(input("Digite um número inteiro: "))

        if num < 2:
            print("Favor digitar um número válido (maior ou igual a 2): ")
            continue
        
        primos = []  # lista para armazenar os números primos

        # Loop verifica números de 2 até num:
        for numero in range(2, num + 1):
            # Número será dado como primo até que se prove o contrário:
            primo = True 

            # Loop para ver se numero é divisível por qualquer número de 2 até numero-1:
            for i in range(2, int(numero ** 0.5) + 1):
                if numero % i == 0:
                    primo = False
                    break
            
            if primo:
                primos.append(numero)

        print(f"Números primos entre 1 e {num}: {primos}")
        break  # Sai do loop após operação bem-sucedida

    except ValueError:
        print("Entrada inválida. Favor inserir número válido.")


