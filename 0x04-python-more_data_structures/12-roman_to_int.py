#!/usr/bin/python3


def roman_to_int(roman_string):
    if type(roman_string) is str:
        romans = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        res = 0
        i = 0
        while i < len(roman_string):
            # Getting value of symbol roman_string[i]
            s1 = romans.get(roman_string[i], -1)

            if i + 1 < len(roman_string):
                # Getting value of symbol roman_string[i + 1]
                s2 = romans.get(roman_string[i + 1], -1)

                # Comparing both values
                if s1 >= s2:
                    # Value of current symbol is greater
                    # or equal to the next symbol
                    res = res + s1
                    i = i + 1
                else:
                    # Value of current symbol is greater
                    # or equal to the next symbol
                    res = res + s2 - s1
                    i = i + 2
            else:
                res = res + s1
                i = i + 1

        return res
    else:
        return 0
