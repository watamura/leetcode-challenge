#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    """
    反転して数値比較
    11511/11511 cases passed (59 ms)
    Your runtime beats 35.07 % of python3 submissions
    Your memory usage beats 82.95 % of python3 submissions (16.4 MB)
    """

    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0:
    #         return False

    #     reverse_int = int(str(x)[::-1])
    #     return x == reverse_int

    """
    反転して文字列比較
    11511/11511 cases passed (50 ms)
    Your runtime beats 73.24 % of python3 submissions
    Your memory usage beats 82.95 % of python3 submissions (16.5 MB)
    """

    # def isPalindrome(self, x: int) -> bool:
    #     # if x < 0:
    #     #     return False

    #     reverse_str = str(x)[::-1]
    #     return str(x) == reverse_str

    """
    反転させずに前後から徐々に比較
    11511/11511 cases passed (50 ms)
    Your runtime beats 73.24 % of python3 submissions
    Your memory usage beats 98.12 % of python3 submissions (16.4 MB)
    """

    # def isPalindrome(self, x: int) -> bool:
    #     str_x = str(x)
    #     for i in range(len(str_x) // 2):
    #         if str_x[i] == str_x[-(i + 1)]:
    #             continue
    #         else:
    #             return False

    #     return True

    """
    回文数の性質を利用
    ※複数回試したら実行時間にばらつきが結構あった
    11511/11511 cases passed (38 ms)
    Your runtime beats 97.92 % of python3 submissions
    Your memory usage beats 39.39 % of python3 submissions (16.5 MB)
    """

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        # 偶数の回文数は11で割り切れる
        if len(str(x)) % 2 == 0 and x % 11 != 0:
            return False

        reverse_str = str(x)[::-1]
        return str(x) == reverse_str


# @lc code=end
