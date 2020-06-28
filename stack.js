class Stack {
    constructor() {
        this.stack = [];
        this.count = 0;
    }

    push(item) {
        this.stack.push(item);
        this.count++;
    }

    pop() {
        if (isEmpty()) return;
        this.count--;
        return this.stack.pop()
    }

    peek() {
        if (isEmpty()) return;
        return this.stack[this.count - 1];
    }

    isEmpty() {
        return this.count === 0;
    }

    size() {
        return this.count;
    }

    clear() {
        this.stack = [];
        this.count = 0;
    }
}