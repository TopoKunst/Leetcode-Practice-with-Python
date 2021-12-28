class Solution:
    '''
    # brute force
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    '''
    def twoSum(self, nums, target):
        # hash table
        num_idx = {}
        for i, n in enumerate(nums):
            # whether we can find the residual
            res = target - n
            if res in num_idx.keys():
                return [num_idx[res], i]
            # add current number to dict
            else:
                num_idx[n] = i

