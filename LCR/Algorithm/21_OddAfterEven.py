"""
    https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/description/
"""


class Solution:
    def trainingPlan(self, actions: List[int]) -> List[int]:
        # edge case
        if len(actions) == 1:
            return actions

        left, right = 0, len(actions) - 1
        while left < right:
            # find first odd number
            while actions[left] % 2 != 0 and left < right:
                left += 1
            # find last even number
            while actions[right] % 2 != 1 and right > left:
                right -= 1
            if actions[left] % 2 == 0 and actions[right] % 2 == 1:
                actions[left], actions[right] = actions[right], actions[left]
                left += 1
                right -= 1

        return actions