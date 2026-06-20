/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) {
            return NULL;
        }

        unordered_map<Node*, Node*> map;
        Node* newHead = new Node(head->val);
        Node* oldPtr = head->next;
        Node* newPtr = newHead;
        map[head] = newHead;

        while (oldPtr) {
            Node* newNode = new Node(oldPtr->val);
            map[oldPtr] = newNode;
            newPtr->next = newNode;

            oldPtr = oldPtr->next;
            newPtr = newPtr->next;
        }

        oldPtr = head;
        newPtr = newHead;
        while (oldPtr) {
            newPtr->random = map[oldPtr->random];

            newPtr = newPtr->next;
            oldPtr = oldPtr->next;
        }

        return newHead;
    }
};
