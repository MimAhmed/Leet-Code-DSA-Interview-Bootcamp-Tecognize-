class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
#Check if value exists
        while(val in nums):
#Remove value at position
            if(nums[i] == val):
                nums.pop(i)
                i-=1 #Step back once since the size has reduced.
            i+=1