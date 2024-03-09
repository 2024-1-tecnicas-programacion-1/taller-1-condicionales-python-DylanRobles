def evaluar(peso, estatura, edad):
    # TODO: Coloca aquí el código del ejercicio 8: Índice de masa corporal
    Imc = peso/(estatura**2)
    if edad < 45 & Imc < 22.0:
        print("El IMC es bajo")
    elif edad < 45 & Imc >= 22.0:
        print("el IMC es medio")
    elif edad >= 45 & Imc < 22.0:
        print("El IMC es medio")
    elif edad >= 45 & Imc >= 22.0:
        print("El IMC es alto")
            
    return "";

if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
