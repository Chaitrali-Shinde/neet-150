class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dic= {}
        # for i in nums:
        #     dic[i]= dic.get(i, 0)+1
        # result=[]
        # myKeys = list(dic.values())
        # myKeys.sort()
        # sorted_dict = {i: dic[i] for i in myKeys}
        # res= list(sorted_dict.keys())
        # for i in range(0, k):
        #     result.append(res[i])

        bucket= [[] for i in range(len(nums)+1)]
        mydic= {}

        for i in nums:
            mydic[i]= mydic.get(i, 0)+1
        result=[]

        for key, val in mydic.items():
            bucket[val].append(key)
        #print(bucket)

        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                result.append(n)
                if(len(result)==k):
                    return result
        
      
