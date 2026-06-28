class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        j=0
        s=0
        ans=0
        dict1={0:1}
        while j<n:
            s+=nums[j]
            if (s-k) in dict1:
                ans+=dict1[(s-k)]
            dict1[s]=dict1.get(s,0)+1
            j+=1

        return ans

