class Node {
    constructor(data, next = null) {
        this.data = data;
        this.next = next;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.size = 0;
    }

    insertAtBeginning(data) {
        this.head = new Node(data, this.head);
        this.size++;
    }

    insertAtEnd(data) {
        let node = new Node(data);
        let current;
        if (this.head === null) {
            this.head = node;
        }
        else {
            current = this.head;
            while (current.next) {
                current = current.next;
            }
            current.next = node;
        }
        this.size++;
    }

    insertAt(data, index) {
        if (index > 0 && index > this.size) {
            return;
        }
        if (index === 0) {
            this.head = new Node(data, this.head);
        }
        const node = new Node(data);
        let current, previous;
        current = this.head;
        let count = 0;
        while (count < index) {
            previous = current;
            count++;
            current = current.next;
        }
        node.next = current;
        previous.next = node;
        this.size++;
    }
    getAt(index) {
        let current = this.head;
        let count = 0;
        while (current) {
            if (count === index) return current;
            current = current.next;
            count++;
        }
    }

    removeAt(index) {

        if (0 < index > this.size) return;
        let current = this.head;
        let previous;
        let count = 0;
        if (index === 0) {
            this.head = current.next;
        }
        else {
            while (count < index) {
                count++;
                previous = current;
                current = current.next;
            }
            previous.next = current.next;
        }
        this.size--;

    }

    printListData() {
        let current = this.head;
        while (current) {
            console.log(current.data);
            current = current.next;
        }
    }
    printSize() {
        console.log(this.size);
    }
}

const ll = new LinkedList();

ll.insertAtBeginning(100);
ll.insertAtBeginning(200);
ll.insertAtEnd(101);
ll.insertAtBeginning(99);
ll.printListData();
ll.removeAt(2);
console.log("____________________________");
ll.printListData();

ll.printSize();