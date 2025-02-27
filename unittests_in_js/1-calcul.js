 function calculateNumber(a, b, type) {
    a = Math.round(a)
    b = Math.round(b)
    if (type === "SUM"){
        return a + b
    }
    if (type === "SUBTRACT"){
        return a - b;
    }
    if (type === "DIVIDE"){
        return a / b;
    }
    else{
        return ("Error")
    }
}

module.exports = calculateNumber;
