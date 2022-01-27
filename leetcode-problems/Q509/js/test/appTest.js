const assert = require('chai').assert;
const { fibIterative, fibRecursive } = require('../app');

const fibVals = fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181];

describe('App', function() {

    describe('fibIterative()', function() {
        fibVals.forEach((value, index) => {
            it(`fibIterative should return ${value}`, function(){
                assert.equal(fibIterative(index), value);
            });
        })
    });

    describe('fibRecursive()', function() {
        fibVals.forEach((value, index) => {
            it(`fibIterative should return ${value}`, function(){
                assert.equal(fibRecursive(index), value);
            });
        })
    });
    
}); 
