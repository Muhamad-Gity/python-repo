
import sys

print(sys.version_info)
print(sys.version)

# Les sequentiations d'une liste
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('Middle two:', a[3:5])
print('All but ends:', a[1:7])

# Les instances str n'ont pas d'encodage binaire associé et
# les instances d'octets n'ont pas d'encodage de texte associé.
# Ceci est un octet parce qu'il est prefixé par la lettre b (binary operator)
b = b'h\x65llo'
print(list(b))
print(b)

# Ceci est une chaine des caratères car il est semblable aux langages humains
c = 'a\u0300 propos'
print(list(c))
print(c)


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of str


print(repr(to_str(b'woo')))
print(repr(to_str('car')))

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of bytes


print(repr(to_bytes(b'soo')))
print(repr(to_bytes('zar')))

