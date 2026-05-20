# Conversor simples de temperatura, Celsius para Fahrenheit.

while True:
    try:
        temperatura_celsius = float(input("Digite a temperatura em celsius: ")) # Valor é convertido para float para permitir números decimais
        break
    except ValueError:
        print("Por favor, insira apenas um número válido.") # Tratamento de erro para garantir que o usuário insira um número válido

temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

print(f"Temperatura em Fahrenheit: {temperatura_fahrenheit}")
