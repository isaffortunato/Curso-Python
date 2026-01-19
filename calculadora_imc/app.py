#imc = peso / (altura * altura)

# imc = peso / (altura*altura)
# imc_formatado = f"{imc:.2f}"

def calcular_imc(peso,altura):
    if peso <= 0 or altura <= 0:
        print("O valor não pode ser igual a zero. Digite um valor válido.")

    imc = peso / (altura**2)
    if imc >= 40:
        classificacao = "obesidade grau III"
    elif 35 <= imc <= 39.9:
        classificacao = "obesidade grau II"
    elif 30 <= imc <= 34.9:
        classificacao = "obesidade grau I"
    elif 25 <= imc <= 29.9:
        classificacao = "sobrepeso"
    elif 18.5 < imc <= 24.9:
        classificacao = "peso normal"
    else:
        classificacao = "baixo peso"

    return f"O seu IMC é {imc:.2f}, isso indica {classificacao}"

peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura: "))

resultado = calcular_imc(peso,altura)
print(resultado)

#abaixo de 18,5 é baixo peso | 18,5 a 24,9 é peso normal (eutrófico)
#25 a 29,9 é sobrepeso | 30 a 34,9 é obesidade Grau I | 35 a 39,9 é obesidade Grau II
#acima de 40 é obesidade Grau III (mórbida)