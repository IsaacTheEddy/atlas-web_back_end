import { createClient } from 'redis';
import { promisify } from 'util'

// Connects to the Redis Database
const client = createClient()
client.on('error', err => console.log(`Redis client not connected to the server: ${err}`))
client.on('connect', () => console.log(`Redis client connected to the server`))

// Promisify
const getAsync = promisify(client.get).bind(client)

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        if (err) {
            console.error(`Error setting value for ${schoolName}: ${err}`);
        } else {
            console.log(`Reply: OK`);
        }
    });
}

async function displaySchoolValue(schoolName) {
    const value = await getAsync(schoolName)
    console.log(value);
        }


displaySchoolValue('Holberton');
setNewSchool("HolbertonSanFrancisco", '100')
displaySchoolValue('HolbertonSanFrancisco')

client.quit();
