var API = (function () {
    var _socket;


    function connectApi(path, connectCallback, positionCallback) {
        // Connect to API
        _socket = new WebSocket("ws://" + path);

        // Setup event handlers
        _socket.onopen = function (event) {
            console.log("Connected to API server!");

            // Listen for messages
            _socket.onmessage = function (event) {
                var data = JSON.parse(event.data);

                if (data.msg === "position") {
                    var position = JSON.parse(data.payload);
                    positionCallback(position);
                } else if (data.msg === 'allPositions') {
                    var positions = data.payload.split(',')
                    for(var position of positions) {
                        positionCallback(position);
                    }
                } else {
                    console.log("Unknown message", data);
                }
            };

            // Listen for socket being closed
            _socket.onclose = function () {
                console.log("Connection to API server lost");
            };

            connectCallback();
        };
    }


    return {
        start: function (path, connectCallback, positionCallback) {
            connectApi(path, connectCallback, positionCallback);
        },

        getHostPosition: function (hostname, callback) {
            _socket.send(JSON.stringify({
                msg: 'getPosition',
                payload: hostname,
            }));
        },

        getAllHostPositions: function(hostnames) {
            _socket.send(JSON.stringify({
                msg: 'getAllHostPositions',
                payload: hostnames,
            }));
        },

        sendMessage: function(position) {
            console.log('sending message with position of ', position)
            _socket.send(JSON.stringify({
                msg: 'position',
                payload: position
            }))
        }
    };
}());
