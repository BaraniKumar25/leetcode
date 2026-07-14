// Last updated: 7/14/2026, 10:11:07 AM
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int expected = n * (n + 1) / 2;

        int actual = 0;
        for(int num : nums){
            actual += num;
        }
        return expected - actual;

    }

}