const sinon = require("sinon");
const chai = require("chai")
const assert = require("assert")
const Utils = require("./utils")
const sendPaymentRequestToApi = require("./6-payment_token");
const getPaymentTokenFromAPI = require("./6-payment_token");

describe(`sendPaymentRequestToApi()`, () =>  {
    it("Should returna succesful response when success is true", (done) => {
        getPaymentTokenFromAPI(true).then(result => {
            assert.equal(result, "{data: 'Successful response from the API' }")
            done();
        })
    })
})

