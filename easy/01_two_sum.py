# 02/12/2024 start_time: 10:19, END: 10:31
from typing import List


# Brute force
# My solution: It's very bad o(n^2) 😢😢
def two_sum(nums: List[int], target: int) -> List[int]:
    indices = []
    for i in range(len(nums)):
        start_item = nums[i]
        for index, num in enumerate(nums):
            if i != index:
                _sum = start_item + num
                if _sum == target:
                    indices = [i, index]
                    return indices
            
        

# One pass (Hashmap) solution

def two_sum2(nums: List[int], target: int) -> List[int]:
    prevMap = {} # val:index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i


print(two_sum2([2,7,11,15], 9))

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result_map = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in result_map:
                return [result_map[diff], index]
            result_map[diff] = index

x = Solution().twoSum([2,7,11,15], 9)
print(x)