class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int max = piles[0];
        for (int pile : piles) {
            if (pile > max) {
                max = pile;
            }
        }

        int low = 1; 

        while (low < max) {
            int mid = (low + max) / 2;

            int sum = 0;
            for (int i = 0; i < piles.length; i++) {
                sum += ((piles[i] + (mid - 1)) / mid);

                if (sum > h) {
                    break;
                }
            }

            if (sum <= h) {
                max = mid;
            }
            else {
                low = mid + 1;
            }
        }

        return low;
    }
}
