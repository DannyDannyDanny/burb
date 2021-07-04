function upload(req, res, next) {
    // save files and details to redis search  db
    const path = req.file.path.replace(/\\/g, "/");
    
    res.json(path);
}

function search(req, res, next){

}

module.exports = {
    upload,
    search
}