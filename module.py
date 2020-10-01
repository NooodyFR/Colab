from math import sqrt, pi

def fct1():
    racine2 = sqrt(2)/2
    print("\nDans le module, la racine de 2, en local, est:", racine2)

def fct2():
    print("Dans module, la valeur de PI, en global, est:", pi)

racine2 = 1.732 # C'est faux, biensûr!
pi = pi

