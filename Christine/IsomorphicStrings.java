class Solution {
    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        int[] sarr = new int[256];
        int[] tarr = new int[256];

        for (int i = 0; i < s.length(); i++) {
            char schar = s.charAt(i);
            char tchar = t.charAt(i);

            if (sarr[schar] != tarr[tchar]) {
                return false;
            }

            sarr[schar] = i + 1;
            tarr[tchar] = i + 1;
        }

        return true;
    }
}
