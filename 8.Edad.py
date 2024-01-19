#Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:
ano=0
mes=0
dia=0
while ano==0 and mes==0 and dia==0: 
    ano=int(input("Ingrese su AÑO de nacimiento aaaa: "))
    mes=int(input("Ingrese su MES de nacimiento mm: "))
    dia=int(input("Ingrese su DIA de nacimiento dd: "))
    if ano>=9999 or ano<0 or mes>12 or mes<0 or dia>31:
        print("---Ingrese correctamente los datos. ¡Vuelva a intentarlo!---")
        ano=0
        mes=0
        dia=0
    else:
        from time import localtime
        t=localtime() #t.tm_mday _mon _year
        dif_ano=t.tm_year-ano
        dif_mes=t.tm_mon-mes
        dif_dia=t.tm_mday-dia
        if dif_mes==0:
            if dif_dia<0:
                print(f"Usted tiene {dif_ano-1} años.")
            else:
                print(f"Usted tiene {dif_ano} años.")
        elif dif_mes>0:
            print(f"Usted tiene {dif_ano} años.")
        else:
            print(f"Usted tiene {dif_ano-1} años.")