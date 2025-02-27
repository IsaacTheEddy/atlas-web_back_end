import * as fs from "node:fs"
import { promisify } from "node:util"

const readFileAsync = promisify(fs.readFile)
const database = process.argv[2]

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
            resolve({Number_of_students: n_o_s,
            CS_students: CS_students,
            SWE_students: SWE_students
            })
        });
    })
}

