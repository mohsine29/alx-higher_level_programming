#!/usr/bin/python3
def no_c(my_string):
    char_list = list(my_string)
    for x in char_list:
        if x == 'c' or x == 'C':
            char_list.remove(x)
            return (''.join(char_list))
