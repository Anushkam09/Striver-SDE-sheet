#best approach
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)
        ind = -1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                ind = i
                break
        print(ind)
        if ind == -1 :
            nums.reverse()
            return
        for i in range(n-1,ind,-1):
            if nums[i] > nums[ind]:
                nums[ind], nums[i] =nums[i], nums[ind]
                break
        nums[ind + 1:] = reversed(nums[ind + 1:])
        