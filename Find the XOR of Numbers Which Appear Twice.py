class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        for num in set(nums):
            result ^= numss
        return result