class Solution {
    public int maxProfit(int[] prices) {

        int lowest_price = Integer.MAX_VALUE;
        int max_profit = 0;

        for (int day = 0; day < prices.length; day++) {
            int current_price = prices[day];

            lowest_price = Math.min(lowest_price, current_price);
            max_profit = Math.max(max_profit, current_price - lowest_price);
        }

        return max_profit;

    }
}