

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def add_elem(seq, val):
    if seq:
        seq.next = ListNode(val, None)
        return seq.next
    else:
        return ListNode(val, None)


class Solution:
    def deleteDuplicates(self, head) -> Optional[ListNode]:

        start = None
        new = start

        while head:

            f = False
            while head and head.next and head.val == head.next:
                head = head.next
                f = True

            if not f and head:
                new = add_elem(new, head.val)

            if head:
                head = head.next

        return start



"""

class Solution {
public:

    inline ListNode* add_elem(ListNode* seq, int val, ListNode** start) {

        if (seq == nullptr) {

            *start = new ListNode(val, nullptr);
            return *start;

        }
        else {

            seq->next = new ListNode(val, nullptr);
            return seq->next;

        }

    }

    ListNode* deleteDuplicates(ListNode* head) {

        ListNode* newnode = nullptr;
        ListNode* start = newnode;

        while (head != nullptr) {

            bool f = false;
            while (head != nullptr && head->next != nullptr && head->val == head->next->val) {
                head = head->next;
                f = true;
            }

            if (!f && head != nullptr)
                newnode = add_elem(newnode, head->val, &start);

            if (head != nullptr) {
                head = head->next;
            }


        }

        return start;

    }
};


"""
