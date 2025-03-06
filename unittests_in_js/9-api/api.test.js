const { expect } = require('chai');
const request = require('request');

describe('Tests index', function() {
  it('returns the correct status code: 200', function(done) {
    request('http://localhost:7865', function(error, response, body) {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });


  it('returns the correct console.log output', function(done) {
    request('http://localhost:7865', function(error, response, body) {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('Tests Cart Page', function() {
  it('returns the correct status code: 200 if id is a number', function(done) {
    request('http://localhost:7865/cart/42', function(error, response, body) {

      expect(response.statusCode).to.equal(200);

      expect(body).to.equal('Payment methods for cart 42');
      done();
    });
  });
  it('returns 404 if id is not a number', function(done) {
    request('http://localhost:7865/cart/atlas', function(error, response, body) {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});
