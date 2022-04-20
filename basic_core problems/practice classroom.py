Feeling = "How are you?"

# print(Feeling.replace("a", "mm"))
# print(Feeling.replace("e", "mm"))
# print(Feeling.replace("i", "mm"))
# print(Feeling.replace("o", "mm"))
# print(Feeling.replace("u", "mm"))
#
# print(Feeling.replace("?", "ss"))

def special():
    special_characters = "?#$"
    for sep_char in special_characters:
        new_Feeling = Feeling.replace(sep_char, "mm")
        print(new_Feeling)

    vowels = "a,e,i,o,u"
    for v in vowels:
        new_Feeling1 = Feeling.replace(v, "ss")
        print(new_Feeling1)

print(special())

