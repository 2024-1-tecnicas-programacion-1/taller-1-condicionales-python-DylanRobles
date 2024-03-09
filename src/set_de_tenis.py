def evaluar(numA, numB):

      
    if numA > numB+2 | numB > numA+2 & numA >= 6 | numB >= 6: 
        print ("El juego ha terminado")
    elif numA < 6 | numB < 6:
        print ("El juego aun no ha terminado")
    elif numA < 0 | numA > 7 | numB < 0 | numB > 7:
        print ("El valor es invalido")
    
    return ""

if __name__ == '__main__':
    print("Los juegos ganaddor por A:", end="")
    num_victorias_a = int(input())
    print("Los juegos ganaddor por B:", end="")
    num_victorias_b = int(input())

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta)
