#instrucciones:
#1. Te pida tus datos como nombre apelidos y edad
#2. cree una curp con los datos ... en realidad son solo la inicial de tu nombre, tu edad y la inicial de tu apellido
#3. agregar cualquier funcion

nombre = input("Escribe tu nombre: ")
apellido_pat = input("Escribe tu apellido paterno: ")
apellido_mat= input("Escribe tu apellido materno: ")
edad = input("Escribe tu edad: ")

a=nombre[0: 1]
b=apellido_pat[0: 1]
c=apellido_mat[0: 1]
d=edad[0: 2]
x=apellido_mat[0:3]
curp = print("Tu CURP es: ",a + d +c + b + x)
