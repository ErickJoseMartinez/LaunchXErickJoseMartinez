## MARK.- Este programa ejecuta un if/else anidados
# condicion_anidada.py

##MARK.- Variables
a = 16
b = 25
c = 27

##MARK.- Se realiza la validación si a es mayor que b
if a > b:
    ##MARK.- si a es mayor que b entonces se valida si b es mayor que c
    if b > c:
        print ("a es mayor que b y b es mayor que c")
    ##MARK.- b es menor que c
    else: 
        print ("a es mayor que b y menor que c")
    ##MARK.- Se valida si a no es mayor que b, si a es igual a b
elif a == b:
    print ("a es igual que b")
    ##MARK.- Se da una resultado final en caso de que a sea menor que b
else:
    print ("a es menor que b")