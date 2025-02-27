const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js')


describe('calculateNumber()', () =>{
    it("Returns sum if a(rounded) and b(rounded) when type SUM is passed", () => {
        expect(calculateNumber(1 ,3,"SUM")).to.equal(4)
        expect(calculateNumber(1 ,3.7,"SUM")).to.equal(5)
        expect(calculateNumber(1.2 ,3.7,"SUM")).to.equal(5)
        expect(calculateNumber(1.5 ,3.7,"SUM")).to.equal(6)
    })
    it("Returns Difference of a(rounded) and b(rounded) when type SUBTRACT is passed", () => {
        expect(calculateNumber(1 ,3,"SUBTRACT")).to.equal(-2)
        expect(calculateNumber(10 ,3.7,"SUBTRACT")).to.equal(6)
        expect(calculateNumber(4.6 ,3.4,"SUBTRACT")).to.equal(2)
        expect(calculateNumber(1.5 ,3.7,"SUBTRACT")).to.equal(-2)
    })
    it("Returns quotient of a(rounded) and b(rounded) when type DIVIDE is passed", () => {
        expect(calculateNumber(1, 1,"DIVIDE")).to.equal(1)
        expect(calculateNumber(4 ,2,"DIVIDE")).to.equal(2)
        expect(calculateNumber(14.7, 5.3 ,"DIVIDE")).to.equal(3)
        expect(calculateNumber(100,0,"DIVIDE")).to.equal('Error')
    })

})
