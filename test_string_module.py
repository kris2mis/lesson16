import string

# #создание контейнера
# ls = [i for i in range(1, 10, 2)]
# print(ls)
#
# ls = [i * 10 for i in range(1, 10, 2)]
# print(ls)
#
# ls = [i * i for i in range(1, 10, 2)]
# print(ls)
#
#
# s = "qwertyuio"
# ls = [i * 3 for i in s]
# print(ls)
#
# #проверить есть ли qri в s
s = "qwertyuio"
STR = "qri"
ls = [i in STR for i in s]
print(ls)

#проверить, все ли TRUE
print(all(ls))
#проверить, есть ли хоть 1 TRUE
print(any(ls))


# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(type(string.ascii_uppercase))
# print()
# print(string.octdigits)
# print(string.digits)
# print(string.hexdigits)
# print()
# print(string.printable)
# print()
# print(string.punctuation)
