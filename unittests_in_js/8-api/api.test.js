const assert = require("assert")
const request = require("request");


describe("Index Page", ()=> {
    it("Should return a 200 status code and reply with a console.log", (done) =>{
        request('http://localhost:7865', (error, response, body) => {
            assert.strictEqual(response.statusCode, 200)
            done();
        });
    });

    it("should return the correct message", (done) => {
        request('http://localhost:7865', (error, response, body) => {
            assert.strictEqual(body, "Welcome to the payment system")
            done();
        });
    });
});
