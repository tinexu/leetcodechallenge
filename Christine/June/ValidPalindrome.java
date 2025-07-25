class Solution {
    public boolean isPalindrome(String s) {
        String newStr = s.toLowerCase();
        String str = newStr.replaceAll("[^a-zA-Z0-9]", "");

        int i = 0;
        int j = str.length() - 1;
        while ((i < j) && (j > i)) {
            if (str.charAt(i) != str.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }

        return true;
    }
}
