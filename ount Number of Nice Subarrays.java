class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        int count = 0;
        int left = 0;
        int right = 0;
        int oddCount = 0;
        int subarrayCount = 0;

        while (right < nums.length) {
            if (nums[right] % 2 == 1) {
                oddCount++;
                subarrayCount = 0;
            }

            
            while (oddCount == k) {
                if (nums[left] % 2 == 1) {
                    oddCount--;
                }
                left++;
                subarrayCount++;
            }

            count += subarrayCount;
            right++;
        }

        return counttt;
    }
}
