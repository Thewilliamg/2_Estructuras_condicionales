#Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a mayor:
n=int(input("Ingrese la CANTIDAD de numeros que va a ordenar: "))
numeros=[]
for i in range(n):
    numeros.append(int(input(f"Ingrese numero {i+1}:")))
numeros.sort(reverse=False)
txt=""
def conversion(k):                              #Definir la funcion conversion para imprimir sin forma vectorial(sin los [])
    return str(k)
numeros_str=[]
for i in range(n):
    numeros_str=list(map(conversion,numeros))   #Usar la funcion 'conversion' para pasar numeros a numeros_str en formato string
    txt=txt+numeros_str[i]+" "                  #Preparar un texto separando valores por espacios
print(f"Lista ordenada: {txt}")