// Dependencies
var express = require('express');
var app = express();
var bodyparser = require('body-parser');
var pg = require('pg');
var server = require('http').Server(app);
var jwt = require('jsonwebtoken');
var token_life = "5 minutes";
var config = require('./config');
/* 
 * Middleware Definitions and Database Connections
 *
 */

// create a client connection
var client={};
var pg_connect_local = function () {  
    pg.connect(config.local_db(process.argv[2]), function(err, body) {
        if(err) {
            console.log("Local connection failed. Make sure the startup script is being invoked with the port of your DB"); 
            client = {warning:"faulty"};
        }
        else {
            client = body;
            console.log("Connected to local database");
        }
    });
};
// connect to the remote databse if the url is available
if(process.env.DATABASE_URL) {
    pg.connect(process.env.DATABASE_URL, function(err, cl) {
        if (err) {
            console.log("Error in remote connection. Attempting local connection");
            pg_connect_local();
        }
        else {
            client = cl;
            console.log("Connected to remote database:\n");
            console.dir(cl.connectionParameters);
        }   
    });
}
// else, try and connect locally
else pg_connect_local(); 


// parsing power if we want it
app.use(bodyparser.urlencoded({ extended: false }));
app.use(bodyparser.json());

var port = process.env.PORT || 8080;

// authentication middleware to attach object to request
var authenticate = function(req,res,next) {
    jwt.verify(req.get('access-key'), config.secret, function(err, body) {
        if(err) req.user = {error:"You are not logged in."};
        else    req.user = body;
        next();
    });
};

/*
 * Routes Definitions and Such
 *
 *
 */
app.get('/', authenticate, function(req, res) {
    if(!req.user.error)
        res.send("<h1> You are logged in as " + req.user.username + " </h1>");
    else
        res.send("<h1> You are not logged in </h1>");
});

// an example of using a router to control a collection of routes
var secure = express.Router();
secure.use(authenticate);
secure.get('/', function(req, res) {
    res.json(req.user); 
});

app.use('/api', secure);
app.post('/register', function(req, res) {
    res.send("<h1>Your token is: " + jwt.sign(req.body, config.secret, {expiresIn: token_life}) + "</h1>");
    console.log("Token handed out for post");
});

/*
 * Don't forget to listen!
 *
 */

server.listen(port, function(connection) {
    console.log("Listening on port " + port);
});

