const express = require("express")

const app = express()
const port = 7865

app.get("/", (req,res) => {
    res.end("Welcome to the payment system")
})

app.get("/cart/:id", (req,res) => {
    if (id === !isNaN){
        console.log("")
    }
    res.end("")
})

app.get("/available_payments", (req, res) => {
    res.json({
      payment_methods: {
        credit_cards: true,
        paypal: false
      }
    });
  });

  app.post("/login", (req, res) => {
    const { userName } = req.body;
    if (!userName) {
      return res.status(400).json({ error: "Username is required" });
    }
    res.json({ message: `Welcome :${userName}` });
  });

app.listen(port, () => {
    console.log(`API available on localhost port ${port}`)
})
