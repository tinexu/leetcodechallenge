class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];
        answer[0] = 1;

        int[] prefix = new int[nums.length];
        prefix[0] = 1;

        for (int i = 1; i < nums.length; i++) {
            answer[i] = answer[i - 1] * nums[i - 1];
        }

        int multiplier = 1;
        for (int i = answer.length - 1; i >= 0; i--) {
            answer[i] = answer[i] * multiplier;
            multiplier = multiplier * nums[i];
        }

        return answer;
    }
}
