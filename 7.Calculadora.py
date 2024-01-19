#Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y división.
#El programa debe recibir como entrada 2 números reales y un operador, que puede ser +, -, * o /.
#La salida del programa debe ser el resultado de la operación.
n1=int(input("Ingrese numero 1: "))
n2=int(input("Ingrese numero 2: "))
o=input("Ingrese el operando:\n\t+ Para suma\n\t- para resta\n\t* para multiplicar\n\t/ para dividir\n\t** para potencia\n")
if o=='+':
    print(f"{n1} + {n2} = {n1+n2}")
elif o=='-':
    print(f"{n1} - {n2} = {n1-n2}")
elif o=='*':
    print(f"{n1} * {n2} = {n1*n2}")
elif o=='/':
    if n2==0:
        print(f"El denominador no puede ser cero - ({n1}/{n2})?.")
    else:
        print(f"{n1} / {n2} = {n1/n2}")
elif o=='**':
    print(f"{n1} ** {n2} = {n1**n2}")
else:
    print("No digitó operador válido, vuelva a intentar.   @ByWilliam")