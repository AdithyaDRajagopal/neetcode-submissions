class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> s;

        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            if (s.count(num)) {
                return true;
            }
            s.insert(num);
        }

        return false;
    }
};