class Solution:
    def max_area(self, height) -> int:

        # Initiaite two pointers on either side
        left , right = 0 , len(height) - 1 
        
        max_area = 0

        while left < right:
            # Work out the max possible area of these pointers, if its bigger than previously saved max area, overwrite it
            max_area = max( max_area , min( height[left] , height[right] ) * (right - left) )

            # Move pointer accordingly, the smaller height has given us the max area that it can contribute
            if height[left] < height[right]:
                left += 1
                continue
            if height[left] > height[right]:
                right -= 1
                continue

            # This only triggers if the heights are the same
            left += 1
            right -=1

        return max_area



sol = Solution()
height = [2,3,4,5,18,17,6]
print(sol.max_area(height)) # 17

height = [1,1]
print(sol.max_area(height)) # 0

height = [1,8,6,2,5,4,8,3,7]
print(sol.max_area(height)) # 49