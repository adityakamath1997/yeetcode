from collections import OrderedDict
class Solution(object):
    def intToRoman(self, num):
        roman_map = {1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"}

        new_map=OrderedDict(sorted(roman_map.items(), reverse=True))
        ans = ''
        for key, value in new_map.items():
            while key <= num:
                ans += value
                num -= key
        return ans






        