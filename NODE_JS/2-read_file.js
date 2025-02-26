import * as fs from "node:fs"

export default function countStudents(path){
    if (path != null){
        try {
            // 'data' Holds the file results for interaction
            const data = fs.readFileSync(path, 'utf-8')
            const lines = data.split('\n')
            const students = lines.slice(1)
            // Minus the header and Null
            const n_o_s = lines.length - 2
            let CS_students = {
                "CS" : 0,
                "List" : []
            }
            let SWE_students = {
                "SWE" : 0,
                "List" : []
            }

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

            process.stdout.write(`NUmber of students: ${(n_o_s)}
            \rNumber of students in CS: ${CS_students["CS"]}. List: ${CS_students["List"]}
            \rNumber of students in SWE: ${SWE_students["SWE"]}. List: ${SWE_students["List"]}\n`)
            // console.log(CS_students)
            // console.log(SWE_students)
        }
        catch (error) {
            process.stderr.write("Cannot load database\n")
        }
    }}

