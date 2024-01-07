#!/usr/bin/python3
def no_c(my_string):
    char_list = [x for x in my_string if x.lower() != 'c']
    return ''.join(char_list)
