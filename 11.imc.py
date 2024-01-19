#Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona, y le entregue su condición de riesgo.
es=float(input("Ingrese la estatura(mtr): "))
pe=float(input("Ingrese el peso(kg): "))
ed=int(input("Ingrese la edad(años): "))
imc=pe/(es**2)
if imc >= 22:
    if ed>=45:
        print(f"IMC = {round(imc,1)}. Condicion de riesgo: ALTO")
    if ed<45:
        print(f"IMC = {round(imc,1)}. Condicion de riesgo: MEDIO")
else:
    if ed>=45:
        print(f"IMC = {round(imc,1)}. Condicion de riesgo: MEDIO")
    if ed<45:
        print(f"IMC = {round(imc,1)}. Condicion de riesgo: BAJO")        