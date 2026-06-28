class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = {}
        n=len(nums)
        for i in nums:
            dict1[i] = dict1.get(i, 0) + 1   

        cnt = n // 2

        for key, value in dict1.items():
            if value >= cnt:
                return key