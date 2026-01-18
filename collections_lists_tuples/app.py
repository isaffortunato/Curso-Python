familia = ["Isabela","Hugo","Arthur","Rafael","Kenia"]

#print(familia[0])
#print(familia[-1])
#print(familia[2:]) retorna a partir do indice 2
#print(familia[2:4]) retorna a partir do indice 2 até o 4, excluindo o 4

#print(familia)
familia[2] = "Turi"
#print(familia)

familia.extend(["Fabiano", "Igor"])
#print(familia)

#insere a informação no local do indice que colocar
familia.insert(4,"Roxy")
#familia.sort() coloca em ordem alfabetica
print(familia)

idade_familia = [26,28,10,10,46]
#idade_familia.sort() coloca em ordem crescente
print(idade_familia)