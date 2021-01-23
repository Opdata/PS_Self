/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {number}
 */
var getDecimalValue = function (head) {
  let sum = 0;
  let mulValue = 0;
  let currentHead = head;

  while (currentHead !== null) {
    if (mulValue === 0) {
      mulValue = 1;
    } else {
      mulValue *= 2;
    }
    currentHead = currentHead.next;
  }

  currentHead = head;

  while (currentHead !== null) {
    if (currentHead.val == 1) {
      sum += mulValue;
    }
    mulValue /= 2;
    currentHead = currentHead.next;
  }

  return sum;
};
