#instrucciones:
#1. Te pida tus datos como nombre, apelidos y edad
#2. cree una curp con los datos ... en realidad son solo la inicial de tu nombre, tu edad y la inicial de tu apellido
#3. agregar cualquier funcion

nombre= input("ingresa tu nombre: ")
apellido= input("ingresa tus apellidos: ")
edad= input  ("¿Que edad tienes? ")
e= nombre[0: 1]
s= apellido[0: 1]
curp= e+edad+s
print(nombre,apellido,edad, curp)
