// attach a local url to the process if we feel
/*if(!process.env.LOCAL_DB_URL) {
    (function() {
    console.log("Attaching to port "+process.argv[2]);
    process.env.LOCAL_DB_URL = "postgres://localhost:"+process.argv[2];
    })(); 
}*/

module.exports = {
    secret: "Coke on a summer day",
    local_db: function(port) {
        return "postgres://localhost:"+port;
    },
}
