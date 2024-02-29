nom=input('Escribe tu nombre: ')
nom_upper = nom.upper()

ap=input('Ingresa tu apellido: ')
ap_upper = ap.upper()

edad=input('Cuantos años tienes? ')

x= nom_upper[0: 1]
y=ap_upper[0: 1]
curp= x+edad+y
print(nom_upper,ap_upper,edad,curp)

print('tu usuario es: ',curp)

crea_contra=input('crea una contraseña: ')

contra=input('ingresa tu contraseña: ')
if contra==crea_contra:
 print('bienvenido',curp)
else:
 print('tu contraseña es incorrecta')
