const express = require('express')
const app = express()

app.get('/status', (req, res) => {
  res.send('Server is running')
})

const PORT = process.env.PORT || 8216;
app.listen(PORT, function () {
  console.log(`push_server listening on port ${PORT}!`)
})

