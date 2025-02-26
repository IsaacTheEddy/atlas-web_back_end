import { response } from "express";
import { Console } from "node:console";
import { request } from "node:http";
import  http  from 'node:http';

const server = http.createServer((request, response) => {
    const {headers, method, url } = request;
    let body = []
    request.on('error', err => {
        consolele.error(err);
    })
    .on('data', chunk => {
        body.push(chunk);
    })
    .on('end', () => {
        body = Buffer.concat(body).toString();

        response.on('error', err => {
            console.error(err)
        });
        response.writeHead(200, {
            "Content-Type" : 'application/json',
            'X-Powered-By' : 'bacon'
        })
        const responeBody = { headers, method, url, body };
        // response.write('<html>>body><h1>Hello, World!</h1></body></html>')
        response.write(JSON.stringify(responeBody))
        response.end();

    });
})
.listen(8080)

console.log("Running")
