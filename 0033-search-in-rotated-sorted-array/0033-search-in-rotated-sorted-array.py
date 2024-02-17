class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        
        while low <= high:
            mid = (low+high) // 2
            guess = nums[mid]
            if guess == target:
                return mid
            
            if guess >= nums[low] :
                if target > guess or target < nums[low]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if target < guess or target > nums[high]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1