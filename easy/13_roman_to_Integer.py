# 02/12/2024


# My Solution
class Solution:
    def romanToInt(self, s: str) -> int:
        value_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        if len(s) == 1:
            return value_map.get(s)
        return_value = 0
        for i, v in enumerate(s):
            try:
                current_value = value_map.get(v)
                next_value = value_map.get(s[i+1])

                _sum = None
                if current_value >= next_value:
                    _sum = current_value
                else:

                    _sum = -current_value
                return_value += _sum
            except IndexError:
                return_value += current_value
        return return_value


# Neetcode solution more precise

def roman_to_int(s: str):
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    res = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            res -= roman[s[i]]
        else:
            res += roman[s[i]]
