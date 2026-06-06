class Solution {
public:
    vector<vector<int>> powerSet;
    vector<int> res;

    void getAllSubsets(vector<int>& nums, int index) {
        if (index == nums.size()) {
            powerSet.push_back({ res });
            return;
        }

        // include elements
        res.push_back(nums[index]);
        getAllSubsets(nums, index + 1);

        // exclude elements
        res.pop_back();
        
        int idx = index + 1;
        while (idx < nums.size() && nums[idx] == nums[idx - 1]) {
            idx++;
        }
        getAllSubsets(nums, idx);
    }

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        getAllSubsets(nums, 0);
        return powerSet;
    }
};
