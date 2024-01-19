#Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por cuántas letras lo es.
p1=input("Inserte palabra 1: ")
p2=input("Inserte palabra 2: ")
num1=len(p1)
num2=len(p2)
dif=num2-num1
if dif==1:
    dif=(f"{abs(dif)} palabra")
else:
    dif=(f"{abs(dif)} palabras")
if num1==num2:
    print(f"Las dos palabras tienen el mismo largo")
elif num1>num2:    
    print(f"La palabra {p1} tiene {dif} mas que la palabra {p2}")
else:
    print(f"La palabra {p2} tiene {dif} mas que la palabra {p1}")