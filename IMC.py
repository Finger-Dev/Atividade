def calcular_imc():
    # Solicita ao usuário seu peso em kg
    peso = float(input("Digite seu peso em kg: "))
    # Solicita ao usuário sua altura em metros
    altura = float(input("Digite sua altura em metros: "))
    
    # Calcula o IMC usando a fórmula
    imc = peso / (altura ** 2)
    
    # Exibe o resultado
    print(f"Seu IMC é: {imc:.2f}")

# Executa a função
calcular_imc()
