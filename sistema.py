from funciones import validador

apellido = input("Ingrese su apellido: ")
nacido = int(input("Ingrese el año de nacimiento: "))
altura = int(input("Ingrese su altura en cm: "))

persona = [apellido, nacido, altura]
resultado = validador(persona)

print ("______________________________________")
print (f"El apellido del usuario es: {apellido}")

if resultado[0]:
    print ("Nacido en 2010 o mas")
else:
     print ("Nacido antes del 2010")

if resultado[1]:
    print ("Altura cumplida")
else:
    print ("Altura no cumplida")

