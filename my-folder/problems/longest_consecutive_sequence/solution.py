class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #time and space complexity is O(n)
        numS= set(nums)
        cnt=0

        for i in nums:
            if((i-1) not in numS):
                cnt2=1
                while (i+cnt2) in numS:
                    cnt2+=1
                cnt= max(cnt, cnt2)
        return cnt

            

        