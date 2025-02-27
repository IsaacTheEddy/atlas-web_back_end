const assert = require('assert');
const calculateNumber = require('./1-calcul.js')


describe('calculateNumber', () =>{
    it("Returns 6 if 1.4 and 4.5 and type SUM are passed", function (){
        assert.strictEqual(calculateNumber("SUM", 1.4, 4.5,), 6);
    })
    it("Returns -4 if 1.4 and 4.5 and type SUBTRACT are passed", function() {
        assert.strictEqual(calculateNumber("SUBTRACT",1.4, 4.5,), -4)
    })
    it("Returns 0.2 if 1.4 and 4.5 and type DIVIDE are passed", function (){
        assert.strictEqual(calculateNumber("DIVIDE",1.4, 4.5,), 0.2);
    })
    it("Returns 'Error' if 1.4 and 0 and type DIVIDE are passed", function() {
        assert.strictEqual(calculateNumber("DIVIDE",1.4, 0),"Error")
    })
});
