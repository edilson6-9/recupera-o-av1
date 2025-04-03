idade = input("Digite sua idade: ")

if idade.isdigit():  # Verifica se a entrada contém apenas números
    print(f"Você tem {idade} anos.")
else:
    print("Você digitou uma idade inválida.")
