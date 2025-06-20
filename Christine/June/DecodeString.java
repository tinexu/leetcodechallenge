class Solution {
    public StringBuilder recurse(String s, int[] index) {
        StringBuilder res = new StringBuilder();
        int num = 0;

        while (index[0] < s.length()) {
            char c = s.charAt(index[0]);

            if (Character.isDigit(c)) {
                num = num * 10 + c - '0';

                index[0]++;
            }
            else if (c == '[') {
                index[0]++;

                StringBuilder innerStr = recurse(s, index);

                for (int i = 0; i < num; i++) {
                    res.append(innerStr);
                }

                num = 0;
            }
            else if (c == ']') {
                index[0]++;

                return res;
            }
            else {
                res.append(c);

                index[0]++;
            }
        }
        
        return res;
    }

    public String decodeString(String s) {
        return recurse(s, new int[]{0}).toString();
    }
}
