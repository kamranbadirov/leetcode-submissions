class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:

                j, h2 = stack.pop()
                w = i - j

                area = max(area, w * h2)
                start = j
            stack.append((start, h))
        while stack:
            j, h = stack.pop()
            w = len(heights) - j
            area = max(area, w * h)
        return area

        