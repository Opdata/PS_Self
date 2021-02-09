/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} m
 * @param {number} n
 * @return {ListNode}
 */
var reverseBetween = function (head, m, n) {
  arr = [];
  reverseArr = [];
  tailArr = [];
  count = 1;
  node = head;

  while (node != null) {
    if (m > count) {
      arr.push(node.val);
    } else if (m <= count && n >= count) {
      reverseArr.push(node.val);
    } else {
      tailArr.push(node.val);
    }
    node = node.next;
    count++;
  }

  arr = arr.concat(reverseArr.reverse()).concat(tailArr);
  node = head;
  count = 0;

  while (node != null) {
    node.val = arr[count];
    node = node.next;
    count++;
  }

  return head;
};
