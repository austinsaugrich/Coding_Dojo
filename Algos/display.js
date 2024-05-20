class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class SLL {
  constructor() {
    this.head = null;
  }

  addFront(value) {
    const newNode = new Node(value);
    newNode.next = this.head;
    this.head = newNode;
    return this.head;
  }

  removeFront() {
    if (this.head === null) {
      return null;
    }
    this.head = this.head.next;
    return this.head;
  }

  front() {
    if (this.head === null) {
      return null;
    }
    return this.head.data;
  }

  display() {
    let current = this.head;
    let result = [];

    while (current !== null) {
      result.push(current.data);
      current = current.next;
    }

    return result.join(", ");
  }
}

let SLL1 = new SLL();
console.log(SLL1.addFront(76));
console.log(SLL1.addFront(2));
console.log(SLL1.display());
console.log(SLL1.addFront(11.41));
console.log(SLL1.display());
