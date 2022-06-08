#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n_list = []
    for n in range(len(my_list)):
        if my_list[n] % 2 == 0:
            n_list.append(True)
        else:
            n_list.append(False)
    return n_list
