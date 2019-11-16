# this won't work (erreur) ==> error : too many values to unpack
ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
ages_descending = sorted(ages, reverse=True)
# old, second_old = ages_descending
# print(old, second_old)

print('================================')
old = ages_descending[0]
second_old = ages_descending[1]
others = ages_descending[2:]
print(old, second_old, others)
# other way (avec une expression étoilée)
old, second_old, *others = ages_descending
print(old, second_old, others)

print('================================')
print('on peut placer l expression etoilée\ndans n importe qu elle ordre')

old, *others, young = ages_descending
print(old, young, others)
print('================================')

*others, second_litle, young = ages_descending
print(young, second_litle, others)
