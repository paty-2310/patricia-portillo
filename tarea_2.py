operacion = input("elige la opracion que deseas realizar (SUMA/RESTA/MULTIPLICACION/DIVISION):").upper()


if operacion == "SUMA": 
    numero1 = float(input("ingrese el primer numero:")) 
    numero2 = float(input("ingrese el segundo numero:")) 
    
    resultado = numero1 + numero2
    
    print("el resultado es:", resultado) 
     