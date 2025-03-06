const request = require("request");
const assert = require("assert");

const url = "http://localhost:7865";

describe("Index Page", () => {
  it("should return status code 200", (done) => {
    request(url, (error, response, body) => {
      assert.strictEqual(response.statusCode, 200);
      done();
    });
  });

  it("should return the correct message", (done) => {
    request(url, (error, response, body) => {
      assert.strictEqual(body, "Welcome to the payment system");
      done();
    });
  });
});

describe("Cart Page", () => {
  it("should return status code 200 when id is a number", (done) => {
    request(url + '/cart/123', (error, response, body) => {
      assert.strictEqual(response.statusCode, 200);
      done();
    });
  });

  it("should return status code 404 when id is not a number", (done) => {
    request(url + '/cart/abc', (error, response, body) => {
      assert.strictEqual(response.statusCode, 404);
      done();
    });
  });
});

describe('Tests payments page', function() {
    it('should return 200 status and an object', function(done) {
      request.get('http://localhost:7865/available_payments', function(error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(JSON.parse(body)).to.deep.equal({
          payment_methods: {
            credit_cards: true,
            paypal: false
          }
        });
        done();
      });
    });
  });

  describe('Tests login page', function() {
    it('should display a welcome greeting', function(done) {
      const options = {
        url: 'http://localhost:7865/login',
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ userName: 'Michael' })
      };

      request(options, function(error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Welcome Michael');
        done();
      });
    });
  });
