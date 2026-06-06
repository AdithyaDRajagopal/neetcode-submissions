class Solution {
public:
    vector<vector<int>> res;

    void getPermutations(vector<int>& nums, int index) {
        if (index == nums.size()) {
            res.push_back({ nums });
            return;
        }

        for (int i = index; i < nums.size(); i++) {
            swap(nums[i], nums[index]);
            getPermutations(nums, index + 1);
            swap(nums[i], nums[index]);
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        getPermutations(nums, 0);
        return res;        
    }
};
