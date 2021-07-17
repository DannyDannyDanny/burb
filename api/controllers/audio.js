function upload(req, res, next) {
    res.json({
        url: req.file.path.replace(/\\/g, "/"),
        filename: req.file.filename,
        originalname: req.file.originalname,
        size: req.file.size
    });
}

function search(req, res, next){

}

module.exports = {
    upload,
    search
}