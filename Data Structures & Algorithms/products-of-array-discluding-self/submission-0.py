class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        runningPrefix = [1] * n
        runningSuffix = [1] * n

        for i in range(1, n):
            runningPrefix[i] = runningPrefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            runningSuffix[i] = runningSuffix[i + 1] * nums[i + 1]

        return [runningPrefix[i] * runningSuffix[i] for i in range(n)]
        
