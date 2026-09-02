class Solution:
    def trap(self, height: List[int]) -> int:
        l_max = r_max = 0
        n = len(height)
        l = [0] * n
        r = [0] * n
        for i in range(n):
            l[i] = l_max
            l_max = max(l_max, height[i])
            j = -i - 1
            r[j] = r_max
            r_max = max(r_max, height[j])
        s = 0
        for i in range(n):
            s += max(min(l[i], r[i]) - height[i], 0)
        return s
        