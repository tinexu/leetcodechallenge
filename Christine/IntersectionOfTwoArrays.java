class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) {
            return intersection(nums2, nums1);
        }

        HashSet<Integer> set = new HashSet<>();
        for (int num : nums1) {
            set.add(num);
        }

        HashSet<Integer> inter = new HashSet<>();
        for (int num : nums2) {
            if (set.contains(num)) {
                inter.add(num);
            }
        }

        int[] result = new int[inter.size()];
        int idx = 0;
        for (Integer x : inter) {
            result[idx++] = x;
        }
        return result;
    }
}
