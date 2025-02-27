import express from "express"
import http from "node:http"

const app = express()
const port = 1245

app.get("/", (req, res) => {
    res.end("Hello Holberton School")
}).listen(port)
