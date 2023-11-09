#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_int = set()
    total = 0
    for num in my_list:
        if num not in unique_int:
            unique_int.add(num)
            total += 1
    return total
