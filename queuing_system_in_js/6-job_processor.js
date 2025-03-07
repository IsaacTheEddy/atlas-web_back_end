var kue = require('kue');
var queue = kue.createQueue({
  redis: {
    host: '127.0.0.1',
    port: 6379
  }
});

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', function(job_data, done) {
  sendNotification(job_data.phoneNumber, job_data.message);
  done();
});
