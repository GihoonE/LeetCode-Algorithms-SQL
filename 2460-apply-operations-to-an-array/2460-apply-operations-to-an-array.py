class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ret = [0]*len(nums)
        ind = 0
        for i in range(len(nums)):
            if i < len(nums)-1:
                if nums[i] == nums[i+1]:
                    nums[i] *= 2
                    nums[i+1] = 0
            if nums[i] != 0:
                ret[ind] = nums[i]
                ind += 1
        return ret