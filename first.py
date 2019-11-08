import sys

print(sys.version_info)
print(sys.version)

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('Middle two:', a[3:5])
print('All but ends:', a[1:7])

# Ceci est byte parce qu'il est prefixé par la lettre b
b = b'h\x65llo'
print(list(b))
print(b)

# Ceci est une chaine des caratères car il est semblable au langages humains
c = 'a\u0300 propos'
print(list(c))
print(c)
