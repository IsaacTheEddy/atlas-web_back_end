import { createClient } from 'redis';

// Connects to the Redis Database
const client = createClient()

client.on('error', err => console.log(`Redis client not connected to the server: ${err}`))
client.on('connect', () => console.log('Redis client connected to the server'))

function publishMessage(message, time) {
    console.log(`About to send: ${message}`);
    setTimeout(() => {
        client.publish("holberton school channel", message, (err, count) => {
            if (err) {
                console.error(`Error ${err}`);
            } else {
                console.log(`About to send ${message}`);
            }
        });
    }, time);
}

// Example usage
const messages = [
    { message: "Holberton Student #1 starts course", time: 1000 },
    { message: "Holberton Student #2 starts course", time: 2000 },
    { message: "KILL_SERVER", time: 3000 },
    { message: "Holberton Student #3 starts course", time: 4000 },
];

messages.forEach(({ message, time }) => {
    publishMessage(message, time);
});

