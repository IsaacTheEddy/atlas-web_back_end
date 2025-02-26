import { response } from 'express'
import http, { request } from 'node:http'
import * as fs from "node:fs"
import { promisify } from 'node:util'


const database = process.argv[2]
const readFileAsync = promisify(fs.readFile)


export async function countStudents(path) {
    return new Promise((resolve, reject) => {
        let CS_students = {
            "CS" : 0,
            "List" : []
        }
        let SWE_students = {
            "SWE" : 0,
            "List" : []
        }
        readFileAsync(path, 'utf-8', (err, data) => {
            if (err){
                reject(new Error('Cannot load the database'))
                return;
        };
            const lines = data.split('\n')
            const students = lines.slice(1)
            // Minus the header and Null
            const n_o_s = lines.length - 2
            students.forEach(student => {
                if (student.includes('CS')) {
                    CS_students["CS"]++;
                    let sum = student.split(",")
                    CS_students["List"].push(" " + sum[0])
                }
                if (student.includes('SWE')) {
                    SWE_students["SWE"]++;
                    let sum = student.split(",")
                    SWE_students["List"].push(" " + sum[0])
                }
            });
            resolve((`NUmber of students: ${(n_o_s)}
        \rNumber of students in CS: ${CS_students["CS"]}. List: ${CS_students["List"]}
        \rNumber of students in SWE: ${SWE_students["SWE"]}. List: ${SWE_students["List"]}`)
        )})
    })
}

const app = http.createServer(async (req, res) => {
    if (req.url === "/students") {
        const results = await countStudents(database)
        res.writeHead(200, {"Content-Type": 'application/json'});
        res.end(`This is a list of our students\n${results}`)
    }
    if (req.url === "/") {
        res.writeHead(200, {"Content-Type": 'application/json'});
        res.end("Hello Holberton School")}
}).listen(1245)
