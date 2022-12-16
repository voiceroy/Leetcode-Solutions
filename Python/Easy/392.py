class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        elif s == t:
            return True

        found = ""
        index = 0

        for char in t:
            if len(found) == len(s):
                break

            if s[index] == char:
                found += char
                index += 1

        return s == found
