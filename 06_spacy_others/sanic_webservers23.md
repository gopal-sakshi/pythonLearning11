# Python webservers

cd /home/gopalakrishnas/Desktop/repos23/others23/pythonLearning11


`python3 -m http.server`
- starts python server listening on 8000 port


`python3 -m http.server 14344`
- listens on 14344 port
- By default Python serves the files located in your current working directory
- http://localhost:14344/


`python3 -m http.server -b 127.0.0.42 8080`
- restrict access to your HTTP server 
- your server will only be accessible from the local machine.

