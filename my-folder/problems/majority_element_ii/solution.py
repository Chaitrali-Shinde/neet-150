class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele1, ele2, cnt1, cnt2= -5,-5,0,0
        for i in range(len(nums)):
            if cnt1==0 and nums[i]!= ele2:
                ele1= nums[i]
                cnt1=1
            elif cnt2==0 and nums[i]!= ele1:
                ele2= nums[i]
                cnt2=1
            elif nums[i]== ele1:
                cnt1+=1
            elif nums[i]== ele2:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
            
        result=[]
        c1, c2=0,0
        for i in range(len(nums)):
            if(nums[i]== ele1):
                c1+=1
            if(nums[i]== ele2):
                c2+=1
        
        min= (len(nums)//3)+1
        if(c1>=min):
            result.append(ele1)
        if(c2>=min):
            result.append(ele2)

        return result

            
