/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function (head) {
  arr = [];
  currentHead = head;

  while (currentHead !== null) {
    reverseArray = [];

    while (reverseArray.length < 2 && currentHead !== null) {
      reverseArray.push(currentHead.val);
      currentHead = currentHead.next;
    }
    reverseArray.reverse();
    arr = arr.concat(reverseArray);
    reverseArray = [];
  }

  currentHead = head;

  arr.forEach((x) => {
    currentHead.val = x;
    currentHead = currentHead.next;
  });

  return head;
};
