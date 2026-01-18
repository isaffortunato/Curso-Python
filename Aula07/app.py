#def big_mac():
#    print("sanduiche big mac")

#big_mac()

def fazer_big_mac(nome):
    print(f"sanduiche big mac {nome}")

#fazer_big_mac("Isabela")
#fazer_big_mac("Hugo")

def fazer_batata(tamanho):
    print(f"batata {tamanho}")

def preparar_refrigerante(tipo,tamanho):
    print(f"{tipo} {tamanho}")

#fazer_big_mac("Isabela")
#fazer_batata("grande")
#preparar_refrigerante("coca", "média")

def fazer_combo_big_mac(nome,tamanho_batata,tipo_refri,tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refri,tamanho_refri)

#fazer_combo_big_mac("Isabela","grande","Coca","Média")

def soma_num(num1,num2):
    return num1 + num2

#resultado = soma_num(15,20)
#print(resultado)

def maior_num(lista_num):
    lista_num.sort()
    lista_num.reverse()
    maior_num = lista_num[0]
    return maior_num

resultado = maior_num([2321,232324,98594,2937,95538237])
print(resultado)