## MARK.- Este programa se revisan fechas
# dates.py
##MARK.- Info del programa
print('Este programa se revisan fechas')

##MARK.- Importación del módulo de fechas.
from datetime import date

##MARK.- Se obtiene e imprime el día actual.
print(date.today())

##MARK.- Se obtiene e imprime el día actual concatenando una cadena.
print("Today's date is: " + str(date.today()))