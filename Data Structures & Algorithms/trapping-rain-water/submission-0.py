class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        l_wall, r_wall = [0] * n, [0] * n
        
        l_wall[0] = height[0]
        for i in range(1, n):
            l_wall[i] = max(l_wall[i - 1], height[i])
        
        r_wall[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            r_wall[i] = max(r_wall[i + 1], height[i])
        
        res = 0
        for i in range(n):
            res += min(l_wall[i], r_wall[i]) - height[i]
        
        return res



        