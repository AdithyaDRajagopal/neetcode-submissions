class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size() - 1;
        int maxArea = INT_MIN;

        while (left < right) {
            int width = right - left;
            int minHeight = min(heights[left], heights[right]);
            int area = minHeight * width;
            maxArea = max(maxArea, area);

            if (minHeight == heights[left]) {
                left ++;
            } else {
                right --;
            }
        }

        return maxArea;
    }
};
