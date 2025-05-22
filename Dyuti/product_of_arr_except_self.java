class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] products = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            products[i] = 1;
        }

        int base = 1;
        for (int i =  0; i < nums.length; i++) {
            products[i] = base;
            base *= nums[i];
        }
        
        int base2 = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            products[i] *= base2;
            base2 *= nums[i];
        }

        return products;
    }
}
