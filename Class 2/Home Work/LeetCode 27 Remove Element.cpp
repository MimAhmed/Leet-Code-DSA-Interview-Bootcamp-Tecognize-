class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i;
        int s = 0;
        int n = nums.size();

        if(n==0){
            return 0;
        }
        for(i=0;i<n;i++){
            if(nums[i]!=val){
                nums[s++]=nums[i];
            }
        }
        return s;
    }
};
