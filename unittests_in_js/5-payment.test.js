const sinon = require("sinon");
const chai = require("chai")
const assert = require("assert")
const Utils = require("./utils")
const sendPaymentRequestToApi = require("./5-payment")
const {expect} = chai

describe("sendPaymentRequestToApi", () => {
    let spy;

    beforeEach(() => {
        spy = sinon.spy(console, "log");
    });

    afterEach(() => {
        spy.restore();
    });
    it("Calls Utils.calculateNumbers with Type(SUM) and 100 and 20", ()=>{
        sendPaymentRequestToApi(100, 20);
        assert.strictEqual(spy.callCount, 1);
        assert.strictEqual(spy.getCall(0).args[0], "The total is: 120");

    });
    it("Calls Utils.calculateNumbers with Type(SUM) and 10 and 10", ()=>{
        sendPaymentRequestToApi(10, 10);
        assert.strictEqual(spy.callCount, 1);
        assert.strictEqual(spy.getCall(0).args[0], "The total is: 20");

    });
});
