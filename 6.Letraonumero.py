#Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. 
#En caso que sea letra, determine si es mayúscula o minúscula.
n=0
cha=""
while n==0: 
    cha=(input("Ingrese caracter: "))
    if len(cha)>1:
        n=0
        print(" - ERROR - Ingrese un solo caracter - @byWilliam")
    else:
        n=1
        if ord(cha)>=48 and ord(cha)<=57: # Del 48 al 57 en ASCII
            print("Es número.")
        elif ord(cha)>=65 and ord(cha)<=90: # Del 65 al 90 en ASCII
            print("Es letra mayúscula.")
        elif ord(cha)>=97 and ord(cha)<=122: # 97 al 122 en ASCII
            print("Es letra minúscula.")
        else:
            print("No es letra ni número.")