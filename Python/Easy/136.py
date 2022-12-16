class Solution:
    def singleNumber(self, nums: list) -> int:
        unique = 0
        for num in nums:
            unique ^= num
        return unique
