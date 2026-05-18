class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int freq = 0, res = 0;
        
        for (int num: nums) {
            if (freq == 0) {
                res = num;
            }

            if (num == res) {
                freq++;
            } else {
                freq--;
            }
        }

        return res;
    }
};