const express = require('express')
const bodyParser = require('body-parser')
const mongoose = require('mongoose')
const webpush = require('web-push')
const cors = require('cors')
const config = require('config')

mongoose.connect(config.get('DB_URL'))
const Schema = mongoose.Schema
const subSchema = Schema({
  userId: String,
  storeId: String,
  endpoint: String,
  publicKey: String,
  auth: String,
})
const Subscribe = mongoose.model('Subscribe', subSchema)

const app = express()
app.use(bodyParser.json())
app.use(cors())
app.use(bodyParser.urlencoded({ extended: true }))

const vapidKeys = {
  publicKey: config.get('PUBLIC_KEY'),
  privateKey: config.get('SECRET_KEY')
}

webpush.setVapidDetails(
  'localhost:8000',
  vapidKeys.publicKey,
  vapidKeys.privateKey
)

app.get('/status', (req, res) => {
  res.send('Server is running')
})

app.post('/subscribe', (req, res) => {
  const newSubscriber = {
    endpoint: req.body.endpoint,
    keys: {
      p256dh: req.body.publicKey,
      auth: req.body.auth
    }
  }

  const { storeId, userId } = req.body
   
  Subscribe.update(
    { userId, storeId },
    {
      storeId,
      userId,
      endpoint: req.body.endpoint,
      publicKey: req.body.publicKey,
      auth: req.body.auth
    },
    { upsert: true } 
  )
  .then(() => { 
    res.send({ success: true, message: 'add success' })    
  })
  .catch(e => {
    res.send({ success: false, message: 'something worng' })
  })
})


const PORT = process.env.PORT || 8080;
app.listen(PORT, function () {
  console.log(`push_server listening on port ${PORT}!`)
})


