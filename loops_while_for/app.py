# i = 1

# while i < 10:
#     print(i)
#     i += 1 #i = i + 1

# print("terminou",i)

criancas = ["Rafa", "Turi"]

##item é o nome da variável que eu escolhi dentro desse for
# for item in criancas:
#     print(item)

# canal = "refatorando"

# # letra: imprime letra por letra, linha por linha, baseado no tamanho do indice
# for letra in canal:
#     print(letra)

# range (intervalo): imprime o intervalo do indice até o 20, contando com o 0 (ou seja, exclui o 20)
# o primeiro número define onde começa, o segundo o limite (stop - é o único obrigatório)
# e o terceiro o intervalo (de 3 em 3)
# for index in range(7,20,3):
#     print(index)

# for index in range(len(criancas)):
#     print(index)

matrix_numeros = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0],
]

for linha in matrix_numeros:
    #print(linha)
    for coluna in linha:
        print(coluna)