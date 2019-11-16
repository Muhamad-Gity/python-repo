# Avoid Striding and Slicing in a Single Expression
x = ['red', 'orange', 'purple', 'white', 'black', 'pink']
odds = x[::2]
evens = x[1::2]
print(odds)
print(evens)

# inverser une chaine de caractère
a = b'mongoose'
b = a[::-1]
print(b)

# slicing and stride together can make confusion
# decaler et sauter dans une liste peut provoquer un malentendu

z = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(z[::2])  # choisir le deuxieme element après le premier dès le debut
print(z[::-2])  # en commençant par le dernier element
# z[2::2]     ==> ['c', 'e', 'g']
# z[-2::-2]   ==> ['g', 'e', 'c', 'a']
# z[-2:2:-2]  ==> ['g', 'e']
# z[2:2:-2]   ==> []
