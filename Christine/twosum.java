class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] index = new int[2];

        for (int i = 0; i < nums.length; i++) {
            int checkNum = target - nums[i];
            if (map.containsKey(checkNum)) {
                index[0] = i;
                index[1] = map.get(checkNum);
                break;
            }
            else {
                map.put(nums[i], i);
            }
        }

        return index;
    }
}
