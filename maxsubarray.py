#better approach
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        max_sum = -999999999 
        for i in range(n):
            now_sum = 0
            for j in range(i,n):
                now_sum += nums[j]
                max_sum = max(max_sum,now_sum)
        return max_sum
    
#best method
#Kadane's algo
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        max_sum = -999999999 
        now_sum = 0
        for i in range(n):
            now_sum += nums[i]
            max_sum = max(max_sum,now_sum)
            if now_sum < 0:
                now_sum = 0
        return max_sum
    

