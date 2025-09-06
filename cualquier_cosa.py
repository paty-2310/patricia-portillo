print("BIENVENIDO AL CNE\n\n") 

inscrito = input("usted es inscrito en el CNE? (SI/NO): ").upper()
edad = int(input("ingrese su edad:")) 

if inscrito == "SI" and edad >= 18:
    print("\n\nusted puede votar")
elif inscrito == "NO" and edad >= 18:
    print("\n\nusted no puede ingresat al cne") 
else:
    print("\n\ndebe cumplir con los requisitos para poder entrar al sistema")