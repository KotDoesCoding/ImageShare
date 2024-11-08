import http.server
import socketserver
import os
import socket
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

vidpath = str(input('insert the path to the video you want. (make sure the video is in the same directory as the python script, and just give the name OF the video. mp4s only.) '))

PORT = 8000

def htmlhandler(videopath: str):
    htmltext = f'''
    <html style="background-color: black; text-align: center;">
    <title>ImageShare</title>
    <body>
        <style>
            .container {{
              position: relative;
            }}

            .center {{
              margin: 0;
              position: absolute;
              top: 50%;
              left: 50%;
              -ms-transform: translate(-50%, -50%);
              transform: translate(-50%, -50%);
            }}
        </style>
    </body>

    <h1 style="color: white;">ImageShare</h1>

    <p style="color: white;">This file has been sent via Kot/Kotinators 'ImageShare' system.</p>
    <p style="color: white;">You can download the video, or watch it.</p>
    <video width="320" height="240" controls>
        <source src="{videopath}" type="video/mp4">
        Your browser does not support the video tag. Update your browser, or use a different one.
    </video>

    <div class="container">
        <div class="center">
            <a href="{videopath}" download>
                <button>Download</button>
            </a>
        </div>
      </div>
    </html>
    '''
    return htmltext

with open('index.html', 'w') as file:
    file.write(htmlhandler(videopath=vidpath))

class MyHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"ready to sent! server address is {ip}:{PORT}")
    httpd.serve_forever()
