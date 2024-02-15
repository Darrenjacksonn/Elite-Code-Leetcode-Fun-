class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = int( str( abs(x) )[::-1] )
        if x > 2**31:
            return 0

        return x*sign



sol = Solution()
x = 123
print(sol.reverse(x)) # 321

x = -123
print(sol.reverse(x)) # -321

x = 120
print(sol.reverse(x)) # 21