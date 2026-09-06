class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            first = nums[i]
            left = i + 1
            right = len(nums) -1 

            while left < right:
                second = nums[left]
                third = nums[right]
                s = first + second + third
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1    
                else:
                    res.append([first, second, third])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res




        