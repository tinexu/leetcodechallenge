class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> checked = new HashSet<Integer>();

        for (int num : nums) {
            if (checked.contains(num)) {
                return true; 
            }
            checked.add(num);
        }
        return false;
    }
}
