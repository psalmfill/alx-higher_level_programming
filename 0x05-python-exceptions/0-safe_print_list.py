#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    total_printed = 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            total_printed += 1
        print()
        return total_printed
    except Exception as e:
        print()
        return total_printed
