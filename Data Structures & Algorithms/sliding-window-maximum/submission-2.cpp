class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res;
        deque<int> dq;
        int l = 0;

        for (int i = 0; i < nums.size(); i++) {
            while (!dq.empty() && nums[dq.back()] <= nums[i]) {
                dq.pop_back();
            }

            dq.push_back(i);

            int window = i - l + 1;
            if (window == k) {
                res.push_back(nums[dq.front()]);
                if (dq.front() == l) {
                    dq.pop_front();
                }
                l++;
            }
        }

        return res;
    }
};
