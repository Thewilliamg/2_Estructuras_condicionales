#Escriba un programa que pida dos números enteros y que calcule la división, indicando si la división es exacta o no.
dividendo=int(input("Dividendo :"))
divisor=int(input("Divisor: "))
if dividendo%divisor==0:
    nn="es"
else:
    nn="no es"
print(f"La division {nn} exacta.\nCociente: {dividendo//divisor}\nResto: {dividendo%divisor}")