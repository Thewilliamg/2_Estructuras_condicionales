#Escriba un programa que indique si un año es bisiesto o no, teniendo en cuenta cuál era el calendario vigente en ese año:
ano=int(input("Ingrese un anno: "))
if ano>=1582:
    if ano%4==0 and (not(ano%100==0) or ano%400==0):
        print(f"{ano} es bisiesto.")
    else:
        print(f"{ano} NO es bisiesto.")
else:
    if ano%4==0:
        print(f"{ano} es bisiesto.")
    else:
        print(f"{ano} NO es bisiesto.")