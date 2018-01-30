import os
import socket
import threading
import time
import SocketServer
from AES_CNV_COOKIE import Cookie, BLOCK_SIZE
from Crypto import Random
from Secret import __FLAG__

host, port = '0.0.0.0', 4444
BUFF_SIZE = 1024

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    allow_reuse_address = True

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def Register(self):
        self.request.sendall("*****************************REGISTER*****************************\n")
        self.request.sendall("Name: ")
        name = self.request.recv(BUFF_SIZE).strip()
        self.request.sendall("Username: ")
        username = self.request.recv(BUFF_SIZE).strip()
        if "root" in username:
            self.request.sendall("Can not register root user!\n")
        else:
            cookie = self.cookie.register(name, username)
            self.request.sendall("Cookie: %s\n" %cookie)
        self.request.sendall("***************************END REGISTER***************************\n")

    def Login(self):
        self.request.sendall("*******************************LOGIN******************************\n")
        self.request.sendall("Cookie: ")
        cookie = self.request.recv(BUFF_SIZE).strip()
        name, username, time = self.cookie.authentication(cookie)
        if username == None:
            self.request.sendall("Don't attack my service, hacker!\n")
            self.request.sendall("***************************LOGIN FALSE****************************\n")
        else:
            self.request.sendall("**************************LOGIN SUCCESS***************************\n")
            self.request.sendall("Welcome CNV service: %s\n" %name)
            self.request.sendall("Username: %s\n" %username)
            self.request.sendall("Time register: %s\n" %time)
            if username != "root":
                self.request.sendall("Sorry! This service support only root user! Please waiting service upgrade.\n")
                return False
            else:
                self.request.sendall("***************************Root Servive***************************\n")
                self.request.sendall("This is flag: %s\n" %__FLAG__)
        return True

    def handle(self):
        self.key = Random.new().read(BLOCK_SIZE)
        self.cookie = Cookie(self.key)
        self.request.settimeout(1)
        self.countuser = 0
        self.request.sendall("***************************CNVService*****************************\n")
        self.request.sendall("* Challenge created by CNV                                       *\n")
        self.request.sendall("* My blog: https://chung96vn.blogspot.com                        *\n")
        self.request.sendall("***************************CNVService*****************************\n")
        while True:
            self.request.sendall("********************Menu********************\n")
            self.request.sendall("* 1 - Register                             *\n")
            self.request.sendall("* 2 - Login                                *\n")
            self.request.sendall("********************************************\n")
            self.request.sendall("Your choice: ")
            try:
                choice = int(self.request.recv(BUFF_SIZE).strip())
            except:
                choice = 0
            if choice == 1:
                if self.countuser < 2:
                    if self.Register():
                        self.countuser += 1
                else:
                    self.request.sendall("Can not register more than two user!\n")
            elif choice == 2:
                self.Login()
                break
            else:
                self.request.sendall("Invalid choice!\n")
				break
def main():
    server = ThreadedTCPServer((host, port), ThreadedTCPRequestHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running in thread:", server_thread.name
    server_thread.join()

if __name__ == '__main__':
    main()
