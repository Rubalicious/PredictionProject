// Dependencies
var express = require('express');
var app = express();
// var pg  = require('pg'); 
var mongoose = require('mongoose');
var server = require('http').Server(app);
// var conString = process.env.ELEPHANTSQL_URL || "postgres://postgres:5000@localhost/database";
var bodyParser = require('body-parser');

// MongoDB
mongoose.connect('mongodb://localhost/rest_test');

// Express
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Routes
app.use('/api', require('./routes/api')); // referencing a file

app.get('/',function(req, res){
  res.send("Hello world");
});

var port = process.env.PORT || 5000;
server.listen(port, function(connection){
  console.log('Listening on port '+ port)
});