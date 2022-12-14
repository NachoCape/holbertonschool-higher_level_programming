#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    i = 0
    if not roman_string or not isinstance(roman_string, str):
        return res
    elif len(roman_string) == 1 and roman_string[0] in dic:
        res = dic[roman_string[0]]
        return res
    rom = roman_string
    while i < len(roman_string):
        if i < len(roman_string)-1 and rom[i + 1] in dic:
            if dic[rom[i]] >= dic[rom[i+1]]:
                res += dic[rom[i]]
                i += 1
            else:
                res += dic[rom[i+1]] - dic[rom[i]]
                i += 2
        else:
            if i == len(roman_string)-1:
                res += dic[rom[i]]
                i += 1
            else:
                return 0
    return res
