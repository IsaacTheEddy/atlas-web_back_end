import readDatabase from "../utils"

class StudentsController {
    async getAllStudents(request, argument) {
        const results = await readDatabase(argument)
        res.end(`This is the list of students\n${results}`)
        return 200
    }

    async getAllStudentsByMajor (request, argument) {
        const results = await readDatabase(argument)
    }
}
