#!/usr/bin/env python3

word = "fish"
def get_plural(noun):

    vowels = "aeiou"
    if noun.endswith(("ch", "sh", "x", "s", "z", "o")):
        noun = noun + "es"
        print(noun)
    
    elif noun.endswith(("f", "fe")):
        split = noun.rsplit("f", 1)
        noun = split[0] + "ves"
        print (noun)
    
    elif noun[-1] == "y" and noun[-2] not in vowels:
       print (noun[:-1] + "ies")
    
    else:
        print(noun + "s")

get_plural(word)