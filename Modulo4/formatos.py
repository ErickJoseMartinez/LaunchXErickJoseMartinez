## MARK.- Este programa se explican los formatos de cadenas
# formatos.py

##MARK.- Formato para incluír variables dentro de una línea de texto.
mass_percentage = '1/6'
print('On the Moon, you would weigh about %s of your weight on Earth' % mass_percentage)
print("""Both sides of the %s get the same amount of sunlight,
    but only one side is seen from %s because
    the %s rotates around its own axis when it orbits %s.""" % ('Moon', 'Earth', 'Moon', 'Earth'))

mass_percentage = '1/6'
print('On the Moon, you would weigh about {} of your weight on Earth'.format(mass_percentage))

print("""You are lighter on the {0}, because on the {0} 
... you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))

