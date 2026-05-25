class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1
        for i in range(len(arr)):
            b = arr[len(arr)-1-i]
            arr[len(arr)-1-i] = max_val
            max_val = max(max_val, b)
        return arr
            