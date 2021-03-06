const express = require("express");

const audioRoutes = require("./routes/audio");

const app = express();


// app.use((req, res, next) => {
//   res.setHeader("Access-Control-Allow-Origin", "*");
//   res.setHeader(
//     "Access-Control-Allow-Methods",
//     "OPTIONS, GET, POST, PUT, PATCH, DELETE"
//   );
//   res.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization");
//   next();
// });

//serve the content straight from the distribution folder (output after npm run build)
app.use(express.static("public"));
app.use('/uploads', express.static('uploads'));


//serve out the api
app.use("/api/audio", audioRoutes);

app.listen(3000);