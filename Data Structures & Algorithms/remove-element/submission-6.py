class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1
        elif len(nums) == 0:
            return 0
        else: 
            val_index = 0
            non_val_index = len(nums) -1
            while val_index <= non_val_index:
                if (nums[val_index] == val) and (nums[non_val_index] != val):
                    nums[val_index], nums[non_val_index] = nums[non_val_index], nums[val_index]
                if (nums[val_index] != val):
                    val_index += 1
                if (nums[non_val_index] == val):
                    non_val_index -= 1
            return val_index