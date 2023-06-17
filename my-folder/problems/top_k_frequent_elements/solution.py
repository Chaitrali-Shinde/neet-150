class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        #we are using bucket sort logic here
        #we have created a bucket of for [[], [], [], ..., []]
        # index indicates the number of occurance which is not greater than the size of the nums, and the value at that index indicates the actual numbers who have that occurance(index no. of occurance)
        bucket= [[] for i in range(len(nums)+1)]
        mydic= {}
        
        #1-->3, 2-->2, 3-->1
        for i in nums:
            mydic[i]= mydic.get(i, 0)+1
        result=[]
        #bucket index represent occurance
        for key, val in mydic.items():
            bucket[val].append(key)
        print(bucket)

        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                result.append(n)
                if(len(result)==k):
                    return result
        
      
