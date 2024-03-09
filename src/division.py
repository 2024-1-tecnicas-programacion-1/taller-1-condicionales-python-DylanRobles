def evaluar(dividendo, divisor):
    # TODO: Coloca aquí el código del ejercicio 3: Division
    cociente = dividendo/divisor
    residuo = dividendo%divisor
        
    if residuo == 0:
        respuesta = "La Division es exacta"    
    else:
        respuesta = "La division no es exacta" 
    return respuesta

if __name__ == '__main__':
    print("Dividendo:", end="")
    dividendo = int(input())
    print("Divisor:", end="")
    divisor = int(input())

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)
