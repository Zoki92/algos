
class BST {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }

    insert(value) {
        let currentNode = this;
        while (true) {
            if (value < currentNode.value) {
                if (currentNode.left === null) {
                    currentNode.left = new BST(value);
                    break;
                }
                else {
                    currentNode = currentNode.left;
                }
            }
            else {
                if (currentNode.right === null) {
                    currentNode.right = new BST(value);
                    break;
                }
                else {
                    currentNode = currentNode.right;
                }
            }
        }
        return this;
    }


    contains(value) {
        let currentNode = this;
        while (currentNode != null) {
            if (currentNode.value > value) {
                currentNode = currentNode.left;
            }
            else if (currentNode.value < value) {
                currentNode = currentNode.right;
            }
            else {
                return true;
            }
        }
        return false;
    }

    remove(value, parentNode = null) {
        let currentNode = this;
        while (currentNode !== null) {
            if (value < currentNode.value) {
                parentNode = currentNode;
                currentNode = currentNode.left;
            }
            else if (value > currentNode.value) {
                parentNode = currentNode;
                currentNode = currentNode.right;
            }
            else {
                // we are dealing with a node that has got 2 children
                // in this case we want to get the min value in the right subtree
                if (currentNode.left !== null && currentNode.right !== null) {
                    currentNode.value = currentNode.right.getMinValue();
                    currentNode.right.remove(currentNode.value, currentNode);
                }
                // coming back to the root node case
                else if (parentNode === null) {
                    if (currentNode.left !== null) {
                        // replacing currentNode value with
                        // the values of the currentNode left node
                        currentNode.value = currentNode.left.value;
                        currentNode.right = currentNode.left.right;
                        currentNode.left = currentNode.left.left;
                    }
                    else if (currentNode.right !== null) {
                        // replacing currentNode value with
                        // the values of the currentNode right node
                        currentNode.value = currentNode.right.value;
                        currentNode.left = currentNode.right.left;
                        currentNode.right = currentNode.right.right;
                    }
                    else {
                        // this is single-node tree; do nothing
                    }
                }
                else if (parentNode.left === currentNode) {
                    parentNode.left = currentNode.left !== null ? currentNode.left : currentNode.right;
                }
                else if (parentNode.right === currentNode) {
                    parentNode.right = currentNode.left !== null ? currentNode.left : currentNode.right;
                }
                break;
            }
        }
        return this;
    }

    getMinValue() {
        let currentNode = this;
        while (currentNode.left !== null) {
            currentNode = currentNode.left;
        }
        return currentNode.value;
    }
}

