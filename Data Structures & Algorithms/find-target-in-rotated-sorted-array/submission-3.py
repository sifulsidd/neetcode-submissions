class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m 
            
            if nums[l] <= nums[m]:
                # target is greater than middle value 
                # target is less than left value
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            
            else:
                # target greater than middle value 
                # target less than left value 
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
                


        return -1