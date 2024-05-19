class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = float('-inf')
        max_here = 1
        min_here = 1
        n = len(nums)

        for i in range(0, n):
            if nums[i] < 0:
                max_here, min_here = min_here, max_here

            max_here = max(nums[i], max_here * nums[i])
            min_here = min(nums[i], min_here * nums[i])

            m = max(m, max_here)

        return i