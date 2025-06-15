class Solution {
    public int characterReplacement(String s, int k) {
        int best = 0;

        HashSet<Character> set = new HashSet<>();

        for (int i = 0; i < s.length(); i++) {
            set.add(s.charAt(i));
        }

        for (char c : set) {
            int count = 0;
            int left = 0;
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == c) {
                    count++;
                }

                while ((i - left + 1) - count > k) {
                    if (s.charAt(left) == c) {
                        count--;
                    }
                    left++;
                }   

                best = Math.max(best, i - left + 1);
            }
        }

        return best;
    }
}
