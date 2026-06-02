class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        vector<int> res;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            if (map.find(complement) != map.end()) {
                res.push_back(map[complement]);
                res.push_back(i);
                break;
            }
            map[nums[i]] = i;   
        }

        return res;
    }
};
