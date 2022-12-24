class Solution:
    def groupAnagrams(self, strs: list) -> list:
        groups = {}

        for word in strs:
            if (key := "".join(sorted(word))) in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return [groups[x] for x in groups]
