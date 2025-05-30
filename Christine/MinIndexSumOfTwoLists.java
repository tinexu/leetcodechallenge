class Solution {
    public static String[] findRestaurant(String[] list1, String[] list2) {
        List<String> res = new ArrayList<>();
        HashMap<String, Integer> map = new HashMap<>();

        for (int i = 0; i < list1.length; i++) {
            map.put(list1[i], i);
        }

        int min = list1.length + list2.length;
        for (int i = 0; i < list2.length; i++) {
            Integer n = map.get(list2[i]);
            if (n != null) {
                if (n + i < min) {
                    min = n + i;
                    res.clear();
                    res.add(list2[i]);
                }
                else if (n + i == min) {
                    res.add(list2[i]);
                }
            }
        }

        return res.toArray(new String[res.size()]);
    }
}
