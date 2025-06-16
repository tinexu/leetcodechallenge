class Solution {
    public int maxArea(int[] height) {
        int len = height.length;

        // int max = height[0];
        // int index = 0;
        // for (int i = 1; i < len; i++) {
        //     if (height[i] > max) {
        //         max = height[i];
        //         index = i;
        //     }
        // }

        int left = 0;
        int right = len - 1;
        
        int best = 0;

        while (left < right) {
            int diff = right - left;
            best = Math.max(best, (diff * Math.min(height[left], height[right])));

            if (height[left] < height[right]) {
                left++;
            }
            else {
                right--;
            }
        }

        return best;
    }
}
