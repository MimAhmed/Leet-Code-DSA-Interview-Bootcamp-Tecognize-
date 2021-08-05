class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[-1] < target:
                return len(nums)
            elif nums[i] == target:
                return i
            elif nums[i] > target and index == 0:
                index = i
                return index