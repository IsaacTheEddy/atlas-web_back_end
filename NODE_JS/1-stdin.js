process.stdin.setEncoding('utf-8')
const prompt_mess = 'Welcome to Holberton School, what is your name?'
console.log(prompt_mess)

process.stdin.on("readable", function (){
    let chunk = process.stdin.read()
    if (chunk != null) {
        process.stdout.write(`Your name is: ${chunk}`)
    }
})

