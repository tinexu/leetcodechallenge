import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        Map<Character, Integer> map1 = new HashMap<>();
        Map<Character, Integer> map2 = new HashMap<>();

        String alphabet = "abcdefghijklmnopqrstuvwxyz";

        // Initialize maps with all letters set to 0
        for (int i = 0; i < alphabet.length(); i++) {
            char c = alphabet.charAt(i);
            map1.put(c, 0);
            map2.put(c, 0);
        }

        // Count characters in s
        for (int j = 0; j < s.length(); j++) {
            char c = s.charAt(j);
            map1.put(c, map1.getOrDefault(c, 0) + 1);
        }

        // Count characters in t
        for (int j = 0; j < t.length(); j++) {
            char c = t.charAt(j);
            map2.put(c, map2.getOrDefault(c, 0) + 1);
        }

        // Compare both maps
        for (int x = 0; x < alphabet.length(); x++) {
            char c = alphabet.charAt(x);
            if (!map1.get(c).equals(map2.get(c))) {
                return false;
            }
        }

        return true;
    }
}
