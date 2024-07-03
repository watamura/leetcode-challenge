#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            j = hashmap.get(target - num)
            if j and j != i:
                return [i, j]

# @lc code=end
