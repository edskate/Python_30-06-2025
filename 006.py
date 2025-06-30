idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
altura = float(input("Digite sua altura: "))
if altura >= 1.70:
    print("Você é alto.")
else:
    print("Você é baixo.")
    
    #  Condicional (if, elif, else)
profissao = input("Digite sua profissão: ")
if profissao.lower() == "engenheiro":
    print("Você é um engenheiro.")
elif profissao.lower() == "médico":
    print("Você é um médico.")
else:
    print("Você não é engenheiro nem médico.")