
function fibIterative(n) {
    if (n === 0) return 0;
    else if (n === 1) return 1;
    else {
        let first = 0;
        let second = 1;
        let fib = 0;
        while(n > 1) {
            fib = first + second;
            first = second;
            second = fib;
            n--;
        }
        return fib;
    }
};

function fibRecursive(n) {
    if (n === 0) return 0;
    else if (n === 1) return 1;
    else return _fibRec_(n-2);
};

function _fibRec_(n, first=0, second=1) {
    if (n == 0) return first + second;
    else return _fibRec_(n-1, second, first + second);
};

module.exports = {
    fibIterative, fibRecursive
}