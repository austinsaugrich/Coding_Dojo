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
}

let SLL1 = new SLL();
console.log(SLL1.addFront(18));
console.log(SLL1.addFront(5));
console.log(SLL1.addFront(73));

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
}

let SLL2 = new SLL();
SLL2.addFront(18);
SLL2.addFront(5);
SLL2.addFront(73);

console.log(SLL2.removeFront());
console.log(SLL2.removeFront());
console.log(SLL2.removeFront());
console.log(SLL2.removeFront());

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
}

let SLL3 = new SLL();
SLL3.addFront(18);
console.log(SLL3.front());
SLL3.removeFront();
console.log(SLL3.front());
