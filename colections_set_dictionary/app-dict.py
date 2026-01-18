#o segundo dado "" pode ser uma lista, um booleano, uma string e etc
meses = {
   "Jan" : "Janeiro",
   "Fev" : "Fevereiro", 
   "Mar" : "Março",
   "Abr" : "Abril", 
   "Mai" : "Maio",
   "Jun" : "Junho",
   "Jul" : "Julho",
   "Ago" : "Agosto",
   "Set" : "Setembro",
   "Out" : "Outubro",
   "Nov" : "Novembro",
   "Dez" : "Dezembro",
}

print(meses["Jun"])
#tb pode ser print(meses.get("Mai")) -> a diferença é que dessa forma, quando não existir, ele retorna "none" e da outra forma ele quebra
#print(meses.get("abc", "frase padrão caso não encontre o primeiro parametro"))