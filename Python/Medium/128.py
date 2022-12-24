class Solution:
    def longestConsecutive(self, nums: list) -> int:
        nums = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in nums:
                next_ = num + 1
                while next_ in nums:
                    next_ += 1
                longest = max(longest, next_ - num)

        return longest
