class LRUCache {
public:
    class Node {
        public:
            int key, val;
            Node *prev, *next;

            Node(int k, int v) {
                key = k;
                val = v;
                prev = next = NULL;
            }
    };

    Node* head = new Node(-1, -1);
    Node* tail = new Node(-1, -1);
    int limit;
    unordered_map<int, Node*> map;

    void addNode(Node *newNode) {
        Node* oldNext = head->next;

        head->next = newNode;
        oldNext->prev = newNode;

        newNode->next = oldNext;
        newNode->prev = head;    
    }

    void deleteNode(Node* oldNode) {
        oldNode->prev->next = oldNode->next;
        oldNode->next->prev = oldNode->prev;
    }

    LRUCache(int capacity) {
        limit = capacity;
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if (map.find(key) == map.end()) {
            // If key not present, return -1
            return -1;
        }

        Node* resNode = map[key];
        int res = resNode->val;

        map.erase(key);
        deleteNode(resNode);

        addNode(resNode);
        map[key] = resNode;
        
        return res;
    }
    
    void put(int key, int value) {
        if (map.find(key) != map.end()) {
            // If key already present, overwrite key
            Node *oldNode = map[key];
            map.erase(key);
            deleteNode(oldNode);
        }

        if (map.size() == limit) {
            // If limit is reached, delete LRU
            map.erase(tail->prev->key);
            deleteNode(tail->prev);
        }

        Node* newNode = new Node(key, value);
        addNode(newNode);
        map[key] = newNode;
    }
};
