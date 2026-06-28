class Solution:
    def majorityElement(self, nums: List[int]) -> int:
     cnt1 = 0
     cand = nums[0]

     for i in nums:
        if cnt1 == 0:
            cnt1 = 1
            cand = i
        elif i == cand:   
            cnt1 += 1
        else:
            cnt1 -= 1     
                
     return cand           
