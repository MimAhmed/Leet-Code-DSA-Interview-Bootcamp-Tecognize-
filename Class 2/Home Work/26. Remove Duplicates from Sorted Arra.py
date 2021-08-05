# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         if (len(nums)==0):
#             return 0
#         index = 0
#         for item in range(len(nums)):
#             if(nums[item]!=nums[index]):
#                 index+=1
#                 nums[index]=nums[item]
#         return index+1

# Using set()
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_set = set()
        element_index = 0

        for num in nums:
            if num not in unique_set:
                nums[element_index] = num
                unique_set.add(num)
                element_index += 1
        return element_index