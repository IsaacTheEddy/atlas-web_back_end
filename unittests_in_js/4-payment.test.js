const sinon = require("sinon");
const chai = require("chai")
const Utils = require("./utils")
const sendPaymentRequestToApi = require("./3-payment")
const {expect} = chai

describe("sendPaymentRequestToApi", () => {
    let spy;

    beforeEach(() => {
        spy = sinon.spy(Utils, "calculateNumber");
    });

    afterEach(() => {
        spy.restore();
    });
    it("Calls Utils.calculateNumbers with Type(SUM) and 100 and 20", ()=>{
        sendPaymentRequestToApi(100, 20);

        expect(spy.calledOnce).to.be.true;

        expect(spy.calledWith("SUM", 100, 20)).to.be.true;
    });
});
