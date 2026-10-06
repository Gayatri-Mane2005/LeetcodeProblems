class Solution:
    def thirdMax(self, nums):
        nums = list(set(nums))  # Remove duplicates
        nums.sort(reverse=True) # Sort descending

        if len(nums) >= 3:
            return nums[2]
        else:
            return nums[0]