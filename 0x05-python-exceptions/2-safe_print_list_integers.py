#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    total_printed = 0
    try:
        for i in range(0,x):
            if type(my_list[i]) is not int:
                continue
            print("{:d}".format(my_list[i]), end="")
            total_printed +=1
        print()
        return total_printed
    except Exception as e:
       raise e