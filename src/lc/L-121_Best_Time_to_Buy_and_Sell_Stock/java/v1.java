class Solution {
        public int maxProfit(int[] prices) {
                int max_profit = 0;
                int lowest_price = Integer.MAX_VALUE;

                for (int day = 0; day < prices.length; day++) {
                        int current_price = prices[day];

                        lowest_price = Math.min(lowest_price, current_price);

                        int current_max_profit = current_price - lowest_price;
                        max_profit = Math.max(max_profit, current_max_profit);
                }

                return max_profit;
        }
}