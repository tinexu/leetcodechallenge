class Solution {
    public int trap(int[] height) {
        int left = 0;
        int right = height.length - 1;

        int lMax = 0;
        int rMax = 0;

        int rain = 0;

        while (left < right) {
            if (height[left] < height[right]) { // guarantees no overestimation
                lMax = Math.max(lMax, height[left]); // rain held barred by lowest boundary

                rain += (lMax - height[left]);

                left++;
            }
            else {
                rMax = Math.max(rMax, height[right]);

                rain += (rMax - height[right]);

                right--;
            }
        }

        return rain;
    }
}
