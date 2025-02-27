function calculateNumber(a, b, type) {
    if (type === "SUM"){
        return Math.round(a) + Math.round(b);
    }
    if (type === "SUBTRACT"){
        return Math.round(a) - Math.round(b);
    }
    if (type === "DIVIDE"){
        return Math.round(a) / Math.round(b);
    }
    else{
        return ("Error")
    }
}

module.exports = calculateNumber;
