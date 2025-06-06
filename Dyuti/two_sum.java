class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] indexes = new int[2];
        for (int i = 0; i < nums.length; i++) {
            int tracker = target - nums[i];
            if (map.containsKey(tracker)) {
                indexes[0] = map.get(tracker);
                indexes[1] = i;
            }
            map.put(nums[i], i);
        }
        return indexes;
    }
}
