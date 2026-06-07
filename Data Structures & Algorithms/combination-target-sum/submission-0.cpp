class Solution {
public:
    vector<vector<int>> res;
    vector<int> combination;
    int sum = 0;
    
    void solve(vector<int>& candidates, int target, int index) {
        if (sum == target) {
            res.push_back({ combination });
            return;
        }

        if (sum > target || index == candidates.size()) {
            return;
        }

        // include
        combination.push_back(candidates[index]);
        sum += candidates[index];
        solve(candidates, target, index);
        sum -= candidates[index];
        combination.pop_back();

        // exclude
        solve(candidates, target, index + 1);    
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        solve(candidates, target, 0);
        return res;  
    }
};
