class Solution:
    def maxArea(self, height: List[int]) -> int:
        # maximum area, left index and right index
        max_area, left, right = 0, 0, len(height)-1

        # iteration
        while left < right:
            h = min(height[left], height[right])
            max_area = max(max_area, h * (right - left))
            left, right = left + (height[left] == h), right - (height[right] == h)

        return max_area