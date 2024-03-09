def evaluar(a, b, c):
   
    if(a+b)< c | (a+c)< b | (b+c)<a:    
        print("el triangulo es invalido")
    elif a==b & a ==c & b==c:
        print("el triangulo es equilatero")
    elif a==b & a!=c & b!=c:
        print("el triangulo es isoceles")
    elif a!=b & b!=c & a!=c:
        print("El triangulo es escaleno")
       
    return ""

if __name__ == '__main__':
    print("a:", end="")
    a = float(input())
    print("b:", end="")
    b = float(input())
    print("c:", end="")
    c = float(input())
        
    respuesta = evaluar(a, b, c)
    print(respuesta)
