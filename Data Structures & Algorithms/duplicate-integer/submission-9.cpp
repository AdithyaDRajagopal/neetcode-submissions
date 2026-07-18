class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> sett(nums.begin(), nums.end());
        return sett.size() != nums.size();
    }
};