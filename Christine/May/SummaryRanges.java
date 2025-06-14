class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> res = new ArrayList<>();

        if (nums.length == 0) {
            return res;
        }

        int firstElement = nums[0];
        int hold = nums[0];

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == hold + 1) {
                hold = nums[i];
            }
            else {
                if (hold == firstElement) {
                    res.add(String.valueOf(hold));
                }
                else {
                    res.add(firstElement + "->" + hold);
                }

                firstElement = nums[i];
                hold = nums[i];
            }
        }

        if (hold == firstElement) {
            res.add(String.valueOf(hold));
        }
        else {
            res.add(firstElement + "->" + hold);
        }

        return res;
    }
}
