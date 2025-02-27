const sinon = require("sinon");
const chai = require("chai")
const assert = require("assert")
const Utils = require("./utils")
const getPaymentTokenFromAPI = require("./6-payment_token");
const { expect } = require("chai")

describe(`sendPaymentRequestToApi()`, () =>  {
    it("Should return a succesful response when success is true", (done) => {
        getPaymentTokenFromAPI(true).then(result => {
            expect(result).to.deep.equal({ data: 'Successful response from the API' });
            done();
        })
    })
})

