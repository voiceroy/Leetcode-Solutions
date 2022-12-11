class Solution:
    def replaceElements(self, arr: list) -> list:
        if len(arr) == 1:
            return [-1]

        result = []
        max_so_far = 0
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] > max_so_far:
                max_so_far = arr[i]
            result.append(max_so_far)

        result.reverse()
        result.append(-1)
        return result
