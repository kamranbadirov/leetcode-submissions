class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            target = 0 - nums[i]
            start = i + 1
            end = len(nums) - 1
            while start < end:
                if nums[start] + nums[end] == target:
                    res.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1

                elif nums[start] + nums[end] > target:
                    end -= 1
                else:
                    start += 1
        return res


        