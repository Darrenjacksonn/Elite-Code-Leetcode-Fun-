class Solution:
    def max_area(self, height) -> int:

        left , right = 0 , len(height) - 1 
        max_area = 0

        while left < right:

            max_area = max( max_area , min( height[left] , height[right] ) * (right - left) )

            if height[left] < height[right]:
                left += 1
                continue
            if height[left] > height[right]:
                right -= 1
                continue

            left += 1
            right -=1

        return max_area