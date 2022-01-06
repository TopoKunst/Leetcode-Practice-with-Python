class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # result
        res = []
        nums.sort()
        n = len(nums)
        for i in range(0, n-2):
            # edge case
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # left and right index
            l, r = i+1, n-1
            while l < r:
                # compute the sum of current 3 elements
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    # eliminate identical element
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -=1
                    # update l and r
                    l += 1
                    r -= 1
                elif s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
        return res

    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # hash table
        num_idx = {}
        # result
        res = []
        for i, n in enumerate(nums):
            # the target
            target = 0 - n
            # transform to a twoSum problem
            idx = self.twoSum(num_idx, target, n)
            if idx:
                res = self.addIt(res, idx)
            else:
                num_idx[n] = i
        return res


    def twoSum(self, num_idx, target, last):
        # if nums is None
        if not num_idx:
            return None
        res = []
        for i, n in num_idx.items():
            # whether we can find the residual
            diff = target - n
            if diff in num_idx.keys():
                res.append([diff, n, last])
        if len(res) > 0:
            return res
        else:
            return None


    def addIt(self, res, idx):
        for item1 in idx:
            # if res is empty, then just add items in idx to res
            if not res:
                res.append(item1)
            # if res is not empty, check if there is duplication
            else:
                flag = True
                for item2 in res:
                    if set(item1) == set(item2):
                        flag = False
                        break
                if flag:
                    res.append(item1)
        return res
    '''