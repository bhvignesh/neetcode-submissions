class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_index = 0
        non_val_index = len(nums) -1
        while val_index <= non_val_index:
            if (nums[val_index] == val):
                nums[val_index], nums[non_val_index] = nums[non_val_index], nums[val_index]
                non_val_index -= 1
            else:
                val_index += 1                
        return val_index