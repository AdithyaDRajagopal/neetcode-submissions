class Solution {
public:
    void getAllSubsets(vector<int>& nums, vector<int>& res, int index, vector<vector<int>>& powerSet) {
        if (index == nums.size()) {
            powerSet.push_back({ res });
            return;
        }

        getAllSubsets(nums, res, index + 1, powerSet);
        res.push_back(nums[index]);
        getAllSubsets(nums, res, index + 1, powerSet);
        res.pop_back();
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> powerSet;
        vector<int> res;
        getAllSubsets(nums, res, 0, powerSet);
        return powerSet;
    }
};
