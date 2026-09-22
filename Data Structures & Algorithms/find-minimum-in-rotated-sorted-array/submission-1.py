class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            print(f"l={l}, r={r}, mid={l + (r-l)//2}")
            if nums[l] < nums[r]:
                break
            mid = l + (r - l) // 2
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
        