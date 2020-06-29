function minHeightBst_1(array) {
    return constructMinHeightBst_1(array, null, 0, array.length - 1);
}

// O(nlogn) time | O(n) space - where n is the length of the array
// this is because the insert method does take logn time 
function constructMinHeightBst_1(array, bst, startIdx, endIdx) {
    if (endIdx < startIdx) return;
    const midIdx = Math.floor((startIdx + endIdx) / 2);
    const valueToAdd = array[midIdx];
    if (bst === null) {
        bst = new BST(valueToAdd);
    }
    else {
        bst.insert(valueToAdd);
    }
    constructMinHeightBst_1(array, bst, startIdx, midIdx - 1);
    constructMinHeightBst_1(array, bst, midIdx + 1, endIdx);
    return bst;
}

function minHeightBst_2(array) {
    return constructMinHeightBst_2(array, null, 0, array.length - 1);
}

// O(n) time | O(n) space
function constructMinHeightBst_2(array, bst, startIdx, endIdx) {
    if (endIdx < startIdx) return;
    const midIdx = Math.floor((endIdx + startIdx) / 2);
    const newBstNode = new BST(array[midIdx]);
    if (bst === null) {
        bst = newBstNode;
    }
    else {
        if (array[midIdx] < bst.value) {
            bst.left = newBstNode;
            bst = bst.left;
        }
        else {
            bst.right = newBstNode;
            bst = bst.right;
        }
    }
    constructMinHeightBst_2(array, bst, startIdx, midIdx - 1);
    constructMinHeightBst_2(array, bst, midIdx + 1, endIdx);
    return bst;
}





class BST {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }

    insert(value) {
        if (value < this.value) {
            if (this.left === null) {
                this.left = new BST(value);
            } else {
                this.left.insert(value);
            }
        } else {
            if (this.right === null) {
                this.right = new BST(value);
            } else {
                this.right.insert(value);
            }
        }
    }
}



const array = [1, 2, 5, 7, 10, 13, 14, 15, 22];

console.log(minHeightBst_2(array));