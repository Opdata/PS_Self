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
var reverseList = function (head) {
  arr = [];
  let currentHead = head;

  while (head !== null) {
    arr.push(head.val);
    head = head.next;
  }

  arr.reverse();
  head = currentHead;
  const arrLength = arr.length;
  let arrIndex = 0;

  while (head !== null) {
    if (arrIndex === arrLength) {
      break;
    }
    head.val = arr[arrIndex];
    arrIndex += 1;
    head = head.next;
  }

  head = currentHead;

  return head;
};
