class Solution {
public:
    int firstUniqChar(string s) {
        queue<int> q;
        unordered_map<char, int> map;

        for (int i = 0; i < s.size(); i++) {
            if (map.find(s[i]) == map.end()) {
                q.push(i);
            }

            map[s[i]]++;
        
            while (!q.empty() && map[s[q.front()]] > 1) {
                q.pop();
            }
        }

        return q.empty() ? -1 : q.front(); 
    }
};