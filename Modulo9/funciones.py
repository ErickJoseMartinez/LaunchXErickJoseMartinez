## MARK.- Este programa se explica las funciones.
# funciones.py

#MARK.- Funciones.
# Defino mi función
def rocket_parts():
    print('payload, propellant, structure')


# Llamo a mi función
# rocket_parts() 
#'payload, propellant, structure'

def rocket_parts():
    return 'payload, propellant, structure'

outrocket = rocket_parts()

print(outrocket)

def distance_from_earth(destination):
    if destination == 'Moon':
        return '238,855'
    else:
        return 'Unable to compute to that destination'

print(distance_from_earth('Moon'))
print(distance_from_earth('Saturn'))

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

print(days_to_complete(238855, 75))
# 132.69722222222222

print(round(days_to_complete(238855, 75)))