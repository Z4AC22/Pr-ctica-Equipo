# Pr-ctica-Equipo

nom=input('Escribe tu nombre: ') = Esta línea solicita al usuario que ingrese su nombre y almacena el valor ingresado en la variable nom.

nom_upper = nom.upper() = Esta línea convierte el valor almacenado en la variable nom a mayúsculas y lo guarda en la variable nom_upper. 

ap=input('Ingresa tu apellido: ') =  Esta línea solicita al usuario que ingrese su apellido y almacena el valor ingresado en la variable ap.

ap_upper = ap.upper() = Esta línea convierte el valor almacenado en la variable ap a mayúsculas y lo guarda en la variable ap_upper.

edad=input('Cuantos años tienes? ') =  Esta línea solicita al usuario que ingrese su edad y almacena el valor ingresado en la variable edad.

x= nom_upper[0: 1] = Esta línea asigna a la variable x el primer carácter del valor almacenado en la variable nom_upper.

y=ap_upper[0: 1] =  Esta línea asigna a la variable y el primer carácter del valor almacenado en la variable ap_upper.

curp= x+edad+y = Esta línea concatena los valores de las variables x, edad y y para formar una cadena de texto que representa una CURP simplificada.

print(nom_upper,ap_upper,edad,curp) = Esta línea imprime en la consola los valores de las variables nom_upper, ap_upper, edad y curp, separados por espacios.

print('tu usuario es: ',curp) = Esta línea imprime en la consola la frase "tu usuario es: " seguida del valor de la variable curp.

crea_contra=input('crea una contraseña: ') = Esta línea solicita al usuario que cree una contraseña y almacena el valor ingresado en la variable crea_contra.

contra=input('ingresa tu contraseña: ') = Esta línea solicita al usuario que cree una contraseña y almacena el valor ingresado en la variable crea_contra.

if contra==crea_contra: = Esta línea verifica si el valor de la variable contra es igual al valor de la variable crea_contra. Si son iguales, se ejecuta el bloque de código siguiente.

 print('bienvenido',curp) = Esta línea imprime en la consola la palabra "bienvenido" seguida del valor de la variable curp.
 
else: = Esta línea se ejecuta si la condición del paso 13 no se cumple, es decir, si el valor de la variable contra no es igual al valor de la variable crea_contra.

 print('tu contraseña es incorrecta') = Esta línea imprime en la consola la frase "tu contraseña es incorrecta".
