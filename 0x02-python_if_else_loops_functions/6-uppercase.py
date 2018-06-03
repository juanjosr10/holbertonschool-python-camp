#!/usr/bin/env python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            var = ord(str[i]) - 32
        else:
            var = ord(str[i])
        print("{}".format(chr(var)), end='')
    print("".format())
    
