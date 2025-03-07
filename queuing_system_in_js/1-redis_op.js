import { createClient } from 'redis';

// Connects to the Redis Database
const client = createClient()
client.on('error', err => console.log(`Redis client not connected to the server: ${err}`))
client.on('connect', () => console.log(`Redis client connected to the server`))

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        if (err) {
            console.error(`Error setting value for ${schoolName}: ${err}`);
        } else {
            console.log(`Reply: OK`);
        }
    });
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        if (err) {
            console.error(`Error getting value for ${schoolName}: ${err}`);
        } else {
            console.log(reply);
        }
    });
}


displaySchoolValue('Holberton');
setNewSchool("HolbertonSanFrancisco", '100')
displaySchoolValue('HolbertonSanFrancisco')

client.quit();
