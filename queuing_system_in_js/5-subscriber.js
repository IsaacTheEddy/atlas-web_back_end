import { createClient } from 'redis';

// Connects to the Redis Database
const client = createClient()

client.on('error', err => console.log(`Redis client not connected to the server: ${err}`))
client.on('connect', () => console.log(`Redis client connected to the server`))

function subscribeToChannel(channel, callback) {
    client.subscribe(channel, (err, count) => {
        if (err) {
            console.error(`Error: ${err}`);
        } else {
            console.log(`Subscribed to ${count} channels`);
        }
    });

    client.on('message', (channel, message) => {
        console.log(`Received message on channel ${channel}: ${message}`);

        if (message === 'KILL_SERVER') {
            client.unsubscribe(channel, () => {
            });
        }
    });

    // Call the callback when subscribed
    callback();
}

function main() {
    subscribeToChannel('holberton school channel', () => {
        console.log("Subscriber initialized. Waiting for messages...");
    });
}

main();
