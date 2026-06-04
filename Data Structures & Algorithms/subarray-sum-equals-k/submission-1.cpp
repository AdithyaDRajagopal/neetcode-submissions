class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int count = 0;
        int prefixSum = 0;
        unordered_map<int, int> map;
        map[0] = 1;

        for (int num: nums) {
            prefixSum += num;
            int diff = prefixSum - k;

            if (map.find(diff) != map.end()) {
                count += map[diff];
            }

            if (map.find(prefixSum) == map.end()) {
                map[prefixSum] = 0;
            }

            map[prefixSum]++;
        }

        return count;
    }
};