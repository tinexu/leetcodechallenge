int maxProfit(int* prices, int pricesSize) {
    int min = prices[0];
    int profit = 0;
    int profit_hold = 0;

    for (int i = 1; i < pricesSize; i++) {
        if (prices[i] < min) {
            min = prices[i];
        }
        else {
            profit_hold = prices[i] - min;
            if (profit_hold  > profit) {
                profit = profit_hold ;
            }
        }
    }

    return profit;
}
