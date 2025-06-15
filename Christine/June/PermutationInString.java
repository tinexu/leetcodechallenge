class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) {
            return false;
        }

        int window_size = s1.length();

        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s1.length(); i++) {
            map.put(s1.charAt(i), map.getOrDefault(s1.charAt(i), 0) + 1);
        }

        int map_size = map.size();
        int count = 0;

        int left = 0;
        for (int right = 0; right < s2.length(); right++) {
            char c = s2.charAt(right);
            if (map.containsKey(c)) {
                map.put(c, map.get(c) - 1);
                if (map.get(c) == 0) {
                    count++;
                }
            }

            if ((right - left + 1) > window_size) {
                if (map.containsKey(s2.charAt(left))) {
                    if (map.get(s2.charAt(left)) == 0) {
                        count--;
                    }
                    map.put(s2.charAt(left), map.get(s2.charAt(left)) + 1);
                }

                left++;
            }

            if (count == map_size) {
                return true;
            }
        }

        return false;
    }
}
