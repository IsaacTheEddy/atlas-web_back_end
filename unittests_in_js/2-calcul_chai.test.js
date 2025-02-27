const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js')


describe('calculateNumber()', () =>{
    it("Returns sum if a(rounded) and b(rounded) when type SUM is passed", () => {
        expect(calculateNumber("SUM",1 ,3,)).to.equal(4)
        expect(calculateNumber("SUM",1 ,3.7,)).to.equal(5)
        expect(calculateNumber("SUM",1.2 ,3.7,)).to.equal(5)
        expect(calculateNumber("SUM",1.5 ,3.7,)).to.equal(6)
    })
    it("Returns Difference of a(rounded) and b(rounded) when type SUBTRACT is passed", () => {
        expect(calculateNumber("SUBTRACT",1 ,3,)).to.equal(-2)
        expect(calculateNumber("SUBTRACT",10 ,3.7,)).to.equal(6)
        expect(calculateNumber("SUBTRACT",4.6 ,3.4,)).to.equal(2)
        expect(calculateNumber("SUBTRACT",1.5 ,3.7,)).to.equal(-2)
    })
    it("Returns quotient of a(rounded) and b(rounded) when type DIVIDE is passed", () => {
        expect(calculateNumber("DIVIDE", 1, 1,)).to.equal(1)
        expect(calculateNumber("DIVIDE", 4 ,2,)).to.equal(2)
        expect(calculateNumber("DIVIDE", 14.7, 5.3 ,)).to.equal(3)
        expect(calculateNumber("DIVIDE", 100,0,)).to.equal('Error')
    })

})
