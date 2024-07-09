#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
import numpy as np


class Solution:
    """
    愚直に実装
    3999/3999 cases passed (59 ms)
    Your runtime beats 6.75 % of python3 submissions
    Your memory usage beats 82.32 % of python3 submissions (16.5 MB)
    """

    # def romanToInt(self, s: str) -> int:
    #     roman_map = {
    #         "M": {
    #             "MMM": 3000,
    #             "MM": 2000,
    #             "M": 1000,
    #         },
    #         "D": {
    #             "DCCC": 800,
    #             "DCC": 700,
    #             "DC": 600,
    #             "D": 500,
    #         },
    #         "C": {
    #             "CM": 900,
    #             "CD": 400,
    #             "CCC": 300,
    #             "CC": 200,
    #             "C": 100,
    #         },
    #         "L": {
    #             "LXXX": 80,
    #             "LXX": 70,
    #             "LX": 60,
    #             "L": 50,
    #         },
    #         "X": {
    #             "XC": 90,
    #             "XL": 40,
    #             "XXX": 30,
    #             "XX": 20,
    #             "X": 10,
    #         },
    #         "V": {
    #             "VIII": 8,
    #             "VII": 7,
    #             "VI": 6,
    #             "V": 5,
    #         },
    #         "I": {
    #             "IX": 9,
    #             "IV": 4,
    #             "III": 3,
    #             "II": 2,
    #             "I": 1,
    #         },
    #     }
    #     answer = 0
    #     while s:
    #         possibility = roman_map[s[0]]
    #         match = next(v for v in possibility if s.startswith(v))
    #         answer += possibility[match]
    #         s = s.removeprefix(match)

    #     return answer

    """
    4を変換
    3999/3999 cases passed (37 ms)
    Your runtime beats 93.64 % of python3 submissions
    Your memory usage beats 82.32 % of python3 submissions (16.5 MB)
    """

    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace(
            "XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        answer = 0
        for letter in s:
            answer += roman_map[letter]
        return answer
        # return sum(roman_map[letter] for letter in s)  # 遅い
        # return np.sum(roman_map[letter] for letter in s) # 遅い(この規模だと？)

# @lc code=end
