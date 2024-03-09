def evaluar(anno):
    # TODO: Coloca aquí el código del ejercicio 3: Division
    bisiesto = anno%4
    regla = anno%400
    if bisiesto != 0 & regla != 0:
        print(anno+" no es bisiesto")
    elif bisiesto == 0 & regla ==0:
        print(anno+"  es bisiesto")
    elif bisiesto == 0 & regla != 0:
        print(anno+" no es bisiesto")
        
    return "";

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)
