import { response } from 'express'
import http, { request } from 'node:http'

const app = http.createServer((req, res) => {
    res.writeHead(200, {"Cntent-Type": 'text/plain'});
    res.end("Hello Holberton School")
}).listen(1245)
