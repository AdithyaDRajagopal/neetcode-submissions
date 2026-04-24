class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagrams;

        for (string s: strs) {
            vector<int> count(26, 0);
            for (char c: s) {
                count[c - 'a']++;
            }
            string hashKey = to_string(count[0]);
            for (int i = 1; i < 26; ++i) {
                hashKey += ',' + to_string(count[i]);
            }
            anagrams[hashKey].push_back(s);

        }

        vector<vector<string>> res;
        for (auto& pair: anagrams) {
            res.push_back(pair.second);
        }
        return res;
    }
};
