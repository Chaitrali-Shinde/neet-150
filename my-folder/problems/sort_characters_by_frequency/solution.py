class Solution:
    def frequencySort(self, s: str) -> str:
        result={}
        for i in s:
            if(i not in result):
                result[i]=1
            else:
                val= result.get(i)
                result[i]= val+1
        value= sorted(result.values())
        sorted_result={}
        ans=""
        for i in value:
            for j in s:
                if result[j] ==i:
                    sorted_result[j]=i
        for key in sorted_result:
            ans+= key* (sorted_result.get(key))

        print(sorted_result)
        ans= ans[::-1]
        return ans

       

