#Los tres lados a, b y c de un triángulo deben satisfacer la desigualdad triangular: 
#cada uno de los lados no puede ser más largo que la suma de los otros dos.
#Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:
#si acaso el triángulo es inválido; y
#si no lo es, qué tipo de triángulo es.
a=float(input("Ingrese lado 'a' del triangulo: "))
b=float(input("Ingrese lado 'b' del triangulo: "))
c=float(input("Ingrese lado 'c' del triangulo: "))
rev1=a+b
rev2=a+c
rev3=b+c
if rev1<c:
    print("No es un triangulo valido")
elif rev2<b:
    print("No es un triangulo válido")
elif rev3<a:
    print("No es un triangulo valido")
else:
    if a==b==c:
        print("Es un triangulo equilatero")
    elif a==b or b==c or c==a:
        print("Es un triangulo isósceles")
    else:
        print("Es un triangulo escaleno")