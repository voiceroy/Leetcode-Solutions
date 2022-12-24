class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        prefix = strs[0]
        for string in strs:
            while not string.startswith(prefix):
                prefix = prefix[:-1]

        return prefix
