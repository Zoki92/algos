class BST {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function validateBst(tree) {
    return validateBstHelper(tree, -Infinity, Infinity);
}


function validateBstHelper(tree, minValue, maxValue) {
    if (tree === null) return true;
    if (tree.value < minValue || tree.value >= maxValue) return false;
    const validateLeftTree = validateBstHelper(tree.left, minValue, tree.value);
    const validateRightTree = validateBstHelper(tree.right, tree.value, maxValue);
    return validateLeftTree && validateRightTree;

}

const root = new BST(10);
root.left = new BST(5);
root.left.left = new BST(2);
root.left.left.left = new BST(1);
root.left.right = new BST(5);
root.right = new BST(15);
root.right.left = new BST(13);
root.right.left.right = new BST(14);
root.right.right = new BST(22);


console.assert(validateBst(root), 'Assertion failed, not valid BST');