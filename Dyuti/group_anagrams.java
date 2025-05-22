class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        List<List<String>> groups = new ArrayList<List<String>>();
        List<String> sort = new ArrayList<String>();

        for (String str : strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String sorted = new String(chars);
            
            int index = -1;
            for (int i = 0; i < sort.size(); i++) {
                if (sort.get(i).equals(sorted)) {
                    index = i;
                    break;
                }
            }
            
            if (index == -1) {
                sort.add(sorted);
                List<String> group = new ArrayList<>();
                group.add(str);
                groups.add(group);
            } else {
                groups.get(index).add(str);
            }
        }

        return groups;
    }
    
}
