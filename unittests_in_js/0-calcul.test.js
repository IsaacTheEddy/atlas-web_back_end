const assert = require('assert');
const calculateNumber = require('./0-calcul.js')


describe('calculateNumber', () =>{
    it("Returns 4 if 1 and 3 are passed", function (){
        assert.strictEqual(calculateNumber(1, 3), 4);
    })
    it("Returns 5 if 1 and 3.7 are passed", function() {
        assert.strictEqual(calculateNumber(1, 3.7), 5)
    })
    it("Returns 5 if 1.2 and 3.7 are passed", function (){
        assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    })
    it("Returns 6 if 1.5 and 3.7 are passed", function() {
        assert.strictEqual(calculateNumber(1.5, 3.7), 6)
    })
});
