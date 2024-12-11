class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> occurred = new HashMap<>();

        for (int current = 0; current < nums.length; current++) {
            int needed = target - nums[current];

            if (occurred.containsKey(needed)) {
                return new int[] {current, occurred.get(needed)};
            }

            occurred.put(nums[current], current);
        }

        return new int[2];
    }
}