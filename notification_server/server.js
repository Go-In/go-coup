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

app.get('/subscribe/list', (req, res) => {
  Subscribe.find({})
  .then(subscribers => res.send(subscribers))
  .catch(error => res.send(error))
})

app.get('/subscribe/list/:storeId', (req, res) => {
  Subscribe.find({ storeId: req.params.storeId })
  .then(subscribers => res.send(subscribers))
  .catch(error => res.send(error))  
})

app.get('/notify/all/', (req, res) => {
  Subscribe.find({ })
  .then(subscribers => {
    subscribers.forEach(sub => {
      const { endpoint, publicKey, auth } = sub
      const pushSub = {
        endpoint,
        keys: {
          p256dh: publicKey,
          auth
        }
      }
      const payload = JSON.stringify({
        title: 'Hello World',
        message: 'Event from GoCoup !'
      })
      webpush.sendNotification(pushSub, payload, {})
    })
    res.send('noti send')
  })
})

app.get('/notify/store/:storeId', (req, res) => {
  Subscribe.find({ storeId: req.params.storeId })
  .then(subscribers => {
    subscribers.forEach(sub => {
      const { endpoint, publicKey, auth } = sub
      const pushSub = {
        endpoint,
        keys: {
          p256dh: publicKey,
          auth
        }
      }
      const payload = JSON.stringify({
        title: 'Hello World',
        message: 'Event from GoCoup !'
      })
      webpush.sendNotification(pushSub, payload, {})
    })
    res.send('noti send')
  })
})

app.get('/subscribe/check/:userId/:storeId', (req, res) => {
  const { storeId, userId } = req.params  
  Subscribe.findOne({ storeId, userId })
  .then(sub => {
    res.send(sub !== null)
  })
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

app.post('/unsubscribe', (req, res) => {
  Subscribe.remove({ userId: req.body.userId, storeId: req.body.storeId })
  .then(() => {
    res.send({ success: true, message: 'unsubscribe success' })
  })
  .catch(e => {
    res.send({ success: false, message: 'something worng' })
  })
})

const PORT = process.env.PORT || 8080;
app.listen(PORT, function () {
  console.log(`push_server listening on port ${PORT}!`)
})

