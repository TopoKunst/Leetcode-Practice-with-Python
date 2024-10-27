class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # dicts: num: index
        dicts = {}
        res = []
        for idx, num in enumerate(nums):
            if target - num not in dicts:
                dicts[num] = idx
            else:
                res += [dicts[target-num], idx]
        return res

solution = Solution()
nums = [3, 2, 4]
targets = 6
res = solution.twoSum(nums, targets)
print(res)