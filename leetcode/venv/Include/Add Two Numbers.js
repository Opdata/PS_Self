/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  let first = '';
  let second = '';
  const head = l1;
  const nodeList = [];
  function Add(head, str) {
    while (head !== null) {
      str += head.val;
      head = head.next;
    }

    return str;
  }

  first = Add(l1, first).split('').reverse().join('');
  second = Add(l2, second).split('').reverse().join('');

  const sum = (BigInt(first) + BigInt(second)).toString();
  const result = sum.split('').reverse();

  result.forEach((x) => {
    x = parseInt(x);
    const Node = new ListNode(x, null);
    nodeList.push(Node);
  });

  let nodeIndex = 1;

  nodeList.forEach((x) => {
    if (nodeIndex === nodeList.length) {
      x.next = null;
    } else {
      x.next = nodeList[nodeIndex];
      nodeIndex++;
    }
  });

  return nodeList[0];
};
