const express = require('express')
const mongoose = require('mongoose')
const config = require('config')

mongoose.connect(config.get('DB_URL'))
const app = express()

app.get('/status', (req, res) => {
  res.send('Server is running')
})

const PORT = process.env.PORT || 8080;
app.listen(PORT, function () {
  console.log(`push_server listening on port ${PORT}!`)
})


