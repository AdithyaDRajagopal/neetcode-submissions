class Solution {
public:
    vector<vector<string>> res;
    vector<string> partitions;

    bool isPalindrome(string s) {
        string s2 = s;
        reverse(s2.begin(), s2.end());
        return s == s2;
    }

    void getAllPartitions(string s) {
        if (s == "") {
            res.push_back(partitions);
            return;
        }
        for (int i = 0; i < s.size(); i++) {
            string part = s.substr(0, i+1);
            if (isPalindrome(part)) {
                partitions.push_back(part);
                getAllPartitions(s.substr(i+1));
                partitions.pop_back();
            }
        }
    }

    vector<vector<string>> partition(string s) {
        getAllPartitions(s);
        return res;
    }
};
