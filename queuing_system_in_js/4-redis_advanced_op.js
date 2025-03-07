import { createClient } from 'redis';

// Connects to the Redis Database
const client = createClient()

client.on('error', err => console.log(`Redis client not connected to the server: ${err}`))
client.on('connect', () => console.log(`Redis client connected to the server`))

function createHash(callback) {
    // Using hset to store values in the hash
    client.hset('HolbertonSchools', ['Portland', 50], (err, reply) => {
        if (err) {
            console.error(`Error ${err}`);
        } else {
            console.log(`Reply: ${reply}`);
        }
    });

    client.hset('HolbertonSchools', ['Seattle', 80], (err, reply) => {
        if (err) {
            console.error(`Error ${err}`);
        } else {
            console.log(`Reply: ${reply}`);
        }
    });

    client.hset('HolbertonSchools', ['New York', 20], (err, reply) => {
        if (err) {
            console.error(`Error ${err}`);
        } else {
            console.log(`Reply ${reply}`);
        }
    });

    client.hset('HolbertonSchools', ['Bogota', 20], (err, reply) => {
        if (err) {
            console.error(`Error ${err}`);
        } else {
            console.log(`Reply:${reply}`);
        }
    });

    client.hset('HolbertonSchools', ['Cali', 40], (err, reply) => {
        if (err) {
            console.error(`Error ${err}`);
        } else {
            console.log(`Reply: ${reply}`);
        }
    });

    client.hset('HolbertonSchools', ['Paris', 2], (err, reply) => {
        if (err) {
            console.error(`Error ${err}`);
        } else {
            console.log(`Reply: ${reply}`);
        }
    });

    // Call the callback when all hset operations are complete
    callback();

}

function displayHash(callback) {

    // Using hgetall to retrieve all fields and values
    client.hgetall('HolbertonSchools', (err, contents) => {
        if (err) {
            console.error('Not working');
        } else {
                console.log(contents)
        }

        // Call the callback when the operation is complete
        callback();
    });
}

function main() {
    createHash(() => {
        displayHash(() => {
            client.quit();
        });
    });
}

main();

