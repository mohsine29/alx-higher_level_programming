def weight_average(my_list=[]):
    if not my_list:
        return 0
    a = 0
    b = 0
    for i in my_list:
        a += i[1]
        x = i[0] * i[1]
        b += x
    return b/a 
