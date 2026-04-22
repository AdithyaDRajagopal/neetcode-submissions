class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashMap;

        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            int complement = target - num;
            if (hashMap.find(complement) != hashMap.end()) {
                return { hashMap[complement], i };
            }
            hashMap.insert({ num, i });
        }

        return {};
    }
};
