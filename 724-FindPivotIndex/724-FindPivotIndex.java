// Last updated: 7/14/2026, 10:10:55 AM
class Solution {
    public int pivotIndex(int[] nums) {
        int sum=0,left=0,right=0;
        for(int i:nums){
            sum=sum+i;
        }
        for(int i=0;i<nums.length;i++){
            right=sum-left-nums[i];
            if(left==right){
                return i;
            }
            left=left+nums[i];
        }
        return -1;
    }
}
