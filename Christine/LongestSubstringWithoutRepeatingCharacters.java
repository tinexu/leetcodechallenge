class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> map = new HashMap<>();

        int index = 0; 
        int len = 0;

        for (int i = 0; i < s.length(); i++) {
            if (map.containsKey(s.charAt(i))) {
                index = (index > (map.get(s.charAt(i)) + 1) ? index : (map.get(s.charAt(i)) + 1));
            }

            map.put(s.charAt(i), i);

            len = (len > (i - index + 1) ? len : (i - index + 1));
        }
        
        return len;
    }
}
