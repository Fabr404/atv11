# Crie um programa que receba a idade de uma pessoa e classifique-a de acordo com as seguintes faixas etárias:
# Criança (0-12 anos)
# Adolescente (13-17 anos)
# Adulto (18-59 anos)
# Idoso (60 anos ou mais)

def classificar_faixa_etaria(idade):
    if idade < 0:
        return "Idade inválida"
    elif idade <= 12:
        return "Criança"
    elif idade <= 17:
        return "Adolescente"
    elif idade <= 59:
        return "Adulto"
    else:
        return "Idoso"

# Receber a idade do usuário
idade = int(input("Digite a idade da pessoa: "))

# Exibir a classificação
print(f"A pessoa é classificada como: {classificar_faixa_etaria(idade)}")
