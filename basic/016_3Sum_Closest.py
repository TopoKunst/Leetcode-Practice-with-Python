class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # result
        res = 0
        diff = 2**31 - 1 # inf
        nums.sort()
        n = len(nums)
        for i in range(0, n - 2):
            # edge case
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # left and right index
            l, r = i + 1, n - 1
            while l < r:
                # compute the sum of current 3 elements
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return target
                elif s > target:
                    if s - target < diff:
                        res = s
                        diff = s - target
                    r -= 1
                elif s < target:
                    if target - s < diff:
                        res = s
                        diff = target - s
                    l += 1
        return res