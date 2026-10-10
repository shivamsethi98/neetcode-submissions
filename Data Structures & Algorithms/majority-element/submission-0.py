from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        checkList = Counter(nums)

        for item in checkList:
            if checkList[item] > len(nums) // 2:
                return item
        return 0