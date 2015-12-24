// Dependencies
var express = require('express');
var app = express();
var pg  = require('pg') 
var mongoose = require('mongoose');
var server = require('http').Server(app);
var conString = process.env.ELEPHANTSQL_URL || "postgres://postgres:5000@localhost/database";


mongoose.connect('mongodb://localhost/rest_test');
//creating a database client
var client = new pg.Client(conString);
client.connect(function(err) {
  if(err) {
    return console.error('could not connect to postgres', err);
  }
  client.query('SELECT NOW() AS "theTime"', function(err, result) {
    if(err) {
      return console.error('error running query', err);
    }
    console.log(result.rows[0].theTime);
    //output: Tue Jan 15 2013 19:12:47 GMT-600 (CST)
    client.end();
  });
});

app.get('/',function(req, res){
  res.send("Hello world");
});
var port = process.env.PORT || 5000;
server.listen(port, function(connection){
  console.log('Listening on port '+ port)
});