## MARK.- En este programa se ven algunos tipos de datos
# types.py
##MARK.- Info del programa
print('En este programa se ven algunos tipos de datos')
##MARK.- Este es un tipo de datos int
planetas_en_el_sistema_solar = 8 # int, plutón era considerado un planeta pero ya es muy pequeño
##MARK.- Este es un tipo de datos flotante o decimal
distancia_a_alfa_centauri = 4.367 # float, años luz
##MARK.- Este es un tipo de datos booleano
puede_despegar = True
##MARK.- Este es un tipo de datos string o caracter
transbordador_que_aterrizo_en_la_luna = "Apollo 11" #string

##MARK.- Se utiliza la funcion type para validar que tipo de datos es una variable
type(distancia_a_alfa_centauri)

print('El tipo de dato de la variable distancia_a_alfa_centauri es: ' + str(type(distancia_a_alfa_centauri)))