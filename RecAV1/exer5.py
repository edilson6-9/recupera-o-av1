# Solicita o ano de nascimento do usuário
ano_nascimento = int(input("Em que ano você nasceu? "))

# Obtém o ano atual
from datetime import datetime
ano_atual = datetime.now().year

# Calcula a idade do usuário
idade = ano_atual - ano_nascimento

# Verifica se o usuário já fez ou fará 18 anos neste ano
if idade == 18:
    print("Você já fez 18 anos este ano.")
elif idade > 18:
    print("Você já fez 18 anos.")
else:
    print(f"Você fará 18 anos em {ano_nascimento + 18}.")
