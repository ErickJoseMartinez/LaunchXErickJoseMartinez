## MARK.- Este programa se explican funciones del metodo String
# cadenas.py

##MARK.- Variables
heading = 'temperatures and facts about the moon'
print(heading.title())

##MARK.- Separar cadenas el default son espacios en blanco
temperatures = '''Daylight: 260 F
... Nighttime: -280 F'''
temperatures.split()

print(temperatures)

##MARK.- indica la posición si encuentra la cadena
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius."""
print(temperatures.find('Moon'))

print(temperatures.find('Mars'))

##MARK.- Indica las veces que se encuentra la cadena
print(temperatures.count('Mars'))

print(temperatures.count('Moon'))

##MARK.- Minusculas
print("The Moon And The Earth".lower())
##MARK.- Mayusculas
print('The Moon And The Earth'.upper())

##MARK.- Separa la cadena y posteriormente si es númerica la pinta
mars_temperature = 'The highest temperature on Mars is about 30 C'
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

##MARK.- Valida el fin de la cadena contra una cadena
if "30 C".endswith("C"):
    print("This temperature is in Celsius")