/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode *prev = NULL;
    // struct ListNode *curr = NULL;
    struct ListNode *next_node = NULL;

    while (head != NULL) {
        next_node = head->next;

        head->next = prev;
        prev = head;
        head = next_node;
    }

    return prev;
}
