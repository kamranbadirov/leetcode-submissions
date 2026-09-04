class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_r = [1] * len(nums)
        r_l = [1] * len(nums)
        running_product = nums[0]
        for i in range(1, len(nums)):
            l_r[i] = running_product
            running_product *= nums[i]
        running_product = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            r_l[i] = running_product
            running_product *= nums[i]

        return [l_r[i] * r_l[i] for i in range(len(nums))]

