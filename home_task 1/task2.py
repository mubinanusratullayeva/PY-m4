from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        refoo = []
        for i in range(len(nums)):
            bar = 0
            for j in range(len(nums)):
                if j != i and nums[j] < nums[i]:
                    bar += 1
            refoo.append(bar)
        return refoo

cl = Solution()

print(cl.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))