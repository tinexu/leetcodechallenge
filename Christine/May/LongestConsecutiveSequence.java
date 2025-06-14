class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }

        int longest = 0;
        for (Integer s : set) {
            if (!set.contains(s - 1)) {
                int count = 1;
                while (set.contains(s + count)) {
                    count++;
                }

                longest = Math.max(count, longest);
            }
        }

        return longest;
    }
}
