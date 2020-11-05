
//You need to initialize node in the PiServer directory before this can be run
//Command line:
//node init

var net = require('net');

var count = 1

var client = new net.Socket();
client.connect(8000, '127.0.0.1', function() {
    console.log('Connected');
});


client.on('data', function(data) {
    while(count <= 20){
        console.log('Received frame ' + count);
        count++;
    }
});