const express = require('express');

const audioController = require('../controllers/audio');
const upload = require('../middleware/upload');

const router = express.Router();


// GET /audio/upload
router.post('/upload', upload, audioController.upload);

module.exports = router;