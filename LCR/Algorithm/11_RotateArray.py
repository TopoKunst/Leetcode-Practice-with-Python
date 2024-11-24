"""
    https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/description/
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # edge case
        if len(nums) == 1:
            return nums[0]

        # [left, mid] <= [mid, right]
        left, mid, right = 0, (len(nums) - 1) // 2, len(nums) - 1
        res = 0
        while True:
            if left == right or nums[left] < nums[right]:
                res = nums[left]
                break
            elif nums[left] < nums[mid]:
                left, right = mid, right
                mid = left + (right - left) // 2
            elif nums[left] > nums[mid]:
                left, right = left, mid
                mid = left + (right - left) // 2
            elif nums[left] == nums[mid]:
                res = min(nums[left:right+1])
                break

        return res


solution = Solution()
nums = [2, 2, 0, 1, 2]
res = solution.findMin(nums)
print(res)



# class Solution:
#     # def findMin(self, nums: List[int]) -> int:
#     def findMin(self, nums):
#
#         l, r = 0, len(nums)-1
#
#         while l < r:
#             m = (l + r) // 2
#             if nums[m] > nums[r]:
#                 l = m + 1
#             elif nums[m] < nums[r]:
#                 r = m
#             else:
#                 r = r - 1
#
#         return nums[l]



