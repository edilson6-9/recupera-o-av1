# Solicita as três notas do usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média das notas
media = (nota1 + nota2 + nota3) / 3

# Verifica se o aluno foi aprovado ou reprovado
if media >= 7:
    print("Aprovado! Média:", media)
else:
    print("Reprovado! Média:", media)
