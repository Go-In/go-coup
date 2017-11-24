const express = require('express')
const mongoose = require('mongoose')
const cors = require('cors')
const config = require('config')

mongoose.connect(config.get('DB_URL'))

const app = express()
app.use(bodyParser.json())
app.use(cors())
app.use(bodyParser.urlencoded({ extended: true }))

const vapidKeys = {
  publicKey: 'BAjY5Vq4p2wwLa-tdde3ip7uBxP02MN_4GTvQv4FDQTCs3b_tWl-eZoqtLhhtp_gPmvnk-CtS4zL4kRyeSb6f6I',
  privateKey: 'UndF242-KapDVhm0nd2qzJaB9BCI7GO7JpJ4vzWgMII'
}

webpush.setVapidDetails(
  'localhost:8000',
  vapidKeys.publicKey,
  vapidKeys.privateKey
)

app.get('/status', (req, res) => {
  res.send('Server is running')
})

const PORT = process.env.PORT || 8080;
app.listen(PORT, function () {
  console.log(`push_server listening on port ${PORT}!`)
})


