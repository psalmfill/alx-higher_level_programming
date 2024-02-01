#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(0, list_length):
            n = my_list_1[i]
            d = my_list_2[i]
            if type(n) not in [int, float] or type(d) not in [int, float]:
                print("wrong type")
                result.append(0)
                continue
            if d == 0:
                print("division by 0")
                result.append(0)
                continue
            result.append(n / d)
        return result
    except Exception:
        print("out of range")
        result.append(0)

    finally:
        return result
