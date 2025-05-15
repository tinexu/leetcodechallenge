class Solution {
    public int maxProfit(int[] prices) {
        int indexBuy = 0;
        int minPrice = prices[0];
        int diff = 0;
        int profit = 0;


        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < minPrice) {
                minPrice = prices[i];
                indexBuy = i;
            } else {

                diff = prices[i] - minPrice;
                if (diff > profit) {
                    profit = diff;
                }
            }
            
        }
        if (indexBuy == (prices.length - 1)) {
            return 0; // this check is not really needed
        } else {
            return profit;
        }

    }
}
