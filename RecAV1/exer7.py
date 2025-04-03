# Solicita dois valores ao usuário
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Usando a condição ternária para verificar o maior valor
maior_valor = valor1 if valor1 > valor2 else valor2

# Exibe o maior valor
print("O maior valor é:", maior_valor)
