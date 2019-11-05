const http = require('http');
const port = 3001;

http.createServer((req,res) => {
    res.writeHead(404, {
        'Content-Type':'text/plain',
    });
    res,statusCode = 200;
    res.write('Lunch Time')
    res.end('End of response\n')
}).listen(port);

console.log(`Server is runnung @ http://localhost:${port}`);