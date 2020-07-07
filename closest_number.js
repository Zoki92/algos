// You are given 3 numbers a, b and x.You need to output the multiple of x which is closest to ab.
// If more than one answer exists, display the smallest one.

function closestNumber(a, b, x) {
    const num = Math.pow(a, b) + x / 2;

    return num - (num % x);
}

console.log(closestNumber(349, 1, 4));