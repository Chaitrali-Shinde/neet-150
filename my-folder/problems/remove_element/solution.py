class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = len(nums)-1
        i = 0

        while j -i >= 1:
            if nums[j] == val:
                j = j-1
              
            else:
                if nums[i] == val:
                    nums[i] = nums[j]
                    nums[j] = val
                    j = j-1
                    i += 1
                if nums[i] != val:
                    i += 1
        if i == j :
            if nums[j]==val:
               
                return i
            else: 
                return i+1
        if i-j ==1:
            return i
