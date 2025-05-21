class Solution {
    public static void rev(int[] arr, int beg, int end) {
        while (beg < end) {
            int temp = arr[beg];
            arr[beg++] = arr[end];
            arr[end--] = temp;
        }
    }

    public static void rotate(int[] nums, int k) {
        int n = nums.length;

        k %= n;

        rev(nums, 0, n - 1);
        rev(nums, 0, k - 1);
        rev(nums, k, n - 1);
    }
}
