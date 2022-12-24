from collections import Counter


class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        if k == len(nums):
            return nums

        return [x[0] for x in Counter(nums).most_common(k)]
