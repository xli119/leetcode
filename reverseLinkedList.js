class LinkedListNode {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
  }

const reverseList = function (head) {
  if (head === null || head.next === null) {
    return head;
  } else {
    let prev = null;
    let cur = head;
    while (cur !== null) {
      let nextNode = cur.next;
      cur.next = prev;
      cur = nextNode;
    }
    return prev;
  }
}

const N1 = new LinkedListNode(1);
const N2 = new LinkedListNode(2);
N1.next = N2;
const N3 = new LinkedListNode(3);
N2.next = N3;

reverseList(N1);
console.log(N3.data, N3.next.data, N2.next.data);
