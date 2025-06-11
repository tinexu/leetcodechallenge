#include <limits.h>

int maxProfit(int* prices, int pricesSize) {
   int minPrice = INT_MAX;
   int max_profit = 0;
   int profit = 0;

    for (int i = 0; i < pricesSize; i++) {
        if (prices[i] < minPrice) {
            minPrice = prices[i];
        }
        profit = prices[i] - minPrice;
        if (profit > max_profit) {
            max_profit = profit;
        }
    }
    return max_profit;
}
