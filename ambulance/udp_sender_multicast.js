// http://stackoverflow.com/questions/6177423/send-broadcast-datagram

var SRC_PORT = 6025
var PORT = 6024
var MULTICAST_ADDR = '192.168.2.255'
var dgram = require('dgram')
var server = dgram.createSocket('udp4')

server.bind(SRC_PORT, function () {
  setInterval(multicastNew, 4000)
})

function multicastNew () {
  var message = new Buffer('Multicast message!')
  server.send(message, 0, message.length, PORT, MULTICAST_ADDR, function () {
    console.log('Sent: "' + message + '"')
  })
}
