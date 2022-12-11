class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        complements = dict()

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in complements:
                return [complements[complement], i]

            complements[nums[i]] = i
