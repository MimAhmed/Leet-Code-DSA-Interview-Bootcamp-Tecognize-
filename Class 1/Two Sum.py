# Solve Using Nested Loop
# Time Complexity: O(n²)
# Space Complexity: O(1)
class Solution(object):
    def twoSum(self, nums, target):
        for start in range(len(nums)):
            for end in range(start+1,len(nums)):
                total =  nums[start]+nums[end]
                if total == target:
                    return (start,end)