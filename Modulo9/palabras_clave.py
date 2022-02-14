## MARK.- Este programa se explican palabras clave de python.
# palabras_clave.py

#MARK.- Palabras Clave.
from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime('Arrival: %A %H:%M')

print(arrival_time())
print(arrival_time(hours=0))

from datetime import timedelta, datetime

def arrival_time(destination='1', hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f'{destination} Arrival: %A %H:%M')

print(arrival_time('Moon'))
print(arrival_time('Orbit', hours=0.13))


def variable_length(*args):
    print(args)

variable_length('one', 'two')
#print(variable_length())
#print(variable_length('one', 'two'))

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f'Total time to launch is {total_minutes} minutes'
    else:
        return f'Total time to launch is {total_minutes/60} hours'

print(sequence_time(4, 14, 18))
print(sequence_time(4, 14, 48))

def variable_length(**kwargs):
    print(kwargs)

variable_length(tanks=1, day='Wednesday', pilots=3)

def crew_members(**kwargs):
    print(f'{len(kwargs)} astronauts assigned for this mission:')
    for title, name in kwargs.items():
        print(f'{title}: {name}')

crew_members(captain='Neil Armstrong', pilot='Buzz Aldrin', command_pilot='Michael Collins')

crew_members(captain='Neil Armstrong', pilot='Buzz Aldrin', pilot='Michael Collins')