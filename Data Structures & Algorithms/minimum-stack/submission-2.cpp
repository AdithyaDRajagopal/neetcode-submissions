class MinStack {
public:
    stack<pair<int, int>> minStack;
    
    void push(int value) {
        int minVal = minStack.empty() ? value : min(minStack.top().second, value);
        minStack.push({ value, minVal });
    }
    
    void pop() {
        minStack.pop();
    }
    
    int top() {
        return minStack.top().first;
    }
    
    int getMin() {
        return minStack.top().second;
    }
};
