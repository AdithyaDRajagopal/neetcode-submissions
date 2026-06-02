class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        unordered_set<int> set;
        vector<int> res;
        int n = grid.size();
        int actualSum = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                actualSum += grid[i][j];
                if (set.find(grid[i][j]) != set.end()) {
                    res.push_back(grid[i][j]);
                }
                set.insert(grid[i][j]);
            }
        }

        int expectedSum = (n*n) * (n*n+1)/2;
        int missing = expectedSum - actualSum + res[0];
        res.push_back(missing);
        return res;
    }
};