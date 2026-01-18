#open("caminho","")

# segundo parâmetro: modo que o arquivo vai ser aberto
# r = leitura / a = append/incrementar / w = write
# x = criar arquivo / r+ = leitura + escrita

# arquivo = open("Aula12/test.txt","r")

# print(arquivo.readable()) #idenfifica se o arquivo pode ser lido ou não
# print(arquivo.read())


arquivo = open("Aula12/test.txt","a")

arquivo.write("\nSQL")
arquivo.close()