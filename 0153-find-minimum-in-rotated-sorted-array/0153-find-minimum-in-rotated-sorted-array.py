class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        min_val = nums[0]
        return min_val