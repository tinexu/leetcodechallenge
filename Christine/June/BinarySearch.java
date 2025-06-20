class Solution {
    public static int bsearch(int[] nums, int target, int low, int high) {
        if (high >= low) {
            int mid = (low + high) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            if (nums[mid] < target) {
                return bsearch(nums, target, mid + 1, high);
            }

            return bsearch(nums, target, low, mid - 1);
        }

        return -1;
    }

    public int search(int[] nums, int target) {
        return bsearch(nums, target, 0, nums.length - 1);
    }
}
