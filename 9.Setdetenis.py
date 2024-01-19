ja=int(input("Juegos ganados por A: "))
jb=int(input("Juegos ganados por B: "))
dif=abs(ja-jb)

if (ja>7) or (jb>7) or (jb==ja and jb==7):    #cualquiera mayor a  ocho queda por fuera
    print("-Resultado invalido-")
elif (ja<6 and jb<6) or (jb==ja and ja==6):   # ambos menor a 6 queda por fuera
    print("El set todavia no termina.")
elif ja>jb:               #ja mayor que jb en 7:
    if ja==7:
        if jb==6 or jb==5:
            print("El ganador es A")
        elif jb<5:
            print("-Resultado invalido-")
    elif dif>1:
        print("El ganador es A")
    else:
        print("El set todavía no termina")
elif jb>ja:               #jb mayor que ja en 7:
    if jb==7:
        if ja==6 or ja==5:
            print("El ganador es B")
        elif ja<5:
            print("-Resultado invalido-")
    elif dif>1:
        print("El ganador es B")
    else:
        print("El set todavía no termina")