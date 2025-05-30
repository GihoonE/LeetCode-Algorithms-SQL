/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let i = n;
    return function() {
        const cur = i;
        i += 1;
        return cur;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */