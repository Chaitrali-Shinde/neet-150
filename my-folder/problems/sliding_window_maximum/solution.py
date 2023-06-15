class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # simple approach but lime limit exceeds
        # res = []
        # for i in range(len(nums)-k+1):
        #     res.append(max(nums[i:i+k]))
        # return res
        output= []
        q= collections.deque()
        l=r=0
        while r<len(nums):
            while q and nums[r]> nums[q[-1]]:
                q.pop()
            q.append(r)
            if l> q[0]:
                q.popleft()
            if r+1>= k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output