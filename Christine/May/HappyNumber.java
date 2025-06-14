class Solution {
    public int squareAndSum(int num) {
        int sum = 0;

        while (num > 0) {
            int digit = num % 10;
            sum += (digit * digit);
            num /= 10;
        }

        return sum;
    }
    public boolean isHappy(int n) {
        HashSet<Integer> sums = new HashSet<>();

        while (n != 1) {
            n = squareAndSum(n);

            if (sums.contains(n)) {
                return false;
            }

            sums.add(n);
        }

        return true;
    }
}
