/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* ptr = head;
        int count = 0;

        // Check if k nodes exists
        while (count < k) {
            if (ptr == NULL) {
                return head;
            }

            ptr = ptr->next;
            count++;
        }

        // Reverse remaining list
        ListNode* prevNode = reverseKGroup(ptr, k);

        // reverse current group
        ptr = head;
        count = 0;

        while (count < k) {
            ListNode* next = ptr->next;
            ptr->next = prevNode;
            prevNode = ptr;
            ptr = next;
            count++;
        }

        return prevNode;
    }
};
