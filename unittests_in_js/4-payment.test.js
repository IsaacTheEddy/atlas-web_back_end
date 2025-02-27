const sinon = require("sinon");
const chai = require("chai")
const Utils = require("./utils")
const sendPaymentRequestToApi = require("./4-payment")
const {expect} = chai

describe("sendPaymentRequestToApi", () => {
    let stub;

    beforeEach(() => {
        stub = sinon.stub(Utils, "calculateNumber").returns(10);
    });

    afterEach(() => {
        stub.restore();
    });
    it("Calls Utils.calculateNumbers with Type(SUM) and 100 and 20", ()=>{
        sendPaymentRequestToApi(100, 20);

        expect(stub.calledOnce).to.be.true;

        expect(stub.calledWith("SUM", 100, 20)).to.be.true;
    });
});
