class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # edge case
        if not nums:
            return 0

        # unique elements
        tail = 0

        # iteration
        for i in range(len(nums)):
            if nums[i] != nums[tail]:
                tail += 1
                nums[tail] = nums[i]

        return tail + 1
