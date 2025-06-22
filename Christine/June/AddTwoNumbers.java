/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *hold = malloc(sizeof(struct ListNode));
    hold->val = 0;
    hold->next = NULL;
    struct ListNode *end = hold;
    
    int carry = 0;
    while ((l1 != NULL) || (l2 != NULL) || (carry != 0)) {
        int d1 = (l1 != NULL) ? l1->val : 0;
        int d2 = (l2 != NULL) ? l2->val : 0;

        int sum = d1 + d2 + carry;

        carry = sum / 10;
        int num = sum % 10;

        struct ListNode *new = malloc(sizeof(struct ListNode));
        new->val = num;
        new->next = NULL;

        end->next = new;
        end = new;
        
        if (l1 != NULL) {
            l1 = l1->next;
        }

        if (l2 != NULL) {
            l2 = l2->next;
        }
    }

    struct ListNode *res = hold->next;
    return res;
}
