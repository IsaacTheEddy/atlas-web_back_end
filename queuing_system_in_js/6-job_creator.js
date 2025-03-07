var kue = require('kue')

// Create a queue
const notificationQueue = kue.createQueue({
  redis: {
    host: '127.0.0.1',
    port: 6379,
  }
});

const job_data = {
    phoneNumber: `9188895552`,
    message: "Validate"
}

function createNotificationJob(phoneNumber, message, callback) {
  const job_data = notificationQueue.create('push_notification_code', {
    phoneNumber: `9188895552`,
    message: "Validate"
  }, (err) => {
    if (err) {
      console.error('Failed to create notification job:', err);
      callback(err);
    } else {
      console.log(`Notification job created: ${job_data.id}`);
      callback(null, job_data.id);
    }
  });
}


createNotificationJob(job_data.phoneNumber, job_data.message, (err, jobId) => {
  if (err) {
    console.error('Error creating job:', err);
  } else {
    console.log(`Created job with ID: ${jobId}`);
  }
});
