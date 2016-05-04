import asyncore, socket, sys

class AsyncUdpReceiver(asyncore.dispatcher):

    def __init__(self, host, port, rservo=None, lservo=None):
        asyncore.dispatcher.__init__(self)
        # open as udp socket
        self.create_socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.bind((host, port))
        if rservo:
            self.rservo = rservo
            self.rservo.start(0)
        if lservo:
            self.lservo = lservo 
            self.lservo.start(0)

    def handle_connect(self):
        pass

    def handle_close(self):
        self.close()

    def handle_read(self):
        msg = self.recv(1024).split()
        print msg
        self.rpwr = float(msg[0])
        self.lpwr = float(msg[1])
        self.rdir = msg[2]
        self.ldir = msg[3]
        if self.rservo and self.lservo:
            self.drive()

    def drive(self):
        self.rservo.set_dir(self.rdir)
        self.lservo.set_dir(self.ldir)
        self.rservo.set_spd(self.rpwr)
        self.lservo.set_spd(self.lpwr)
        print "driving {0}@{1}  {2}@{3}".format(
            self.rpwr, self.rdir, self.lpwr, self.ldir)


if __name__ == "__main__":

    server = AsyncUdpReceiver(sys.argv[1], 5000)
    print "Waiting for data..."
    asyncore.loop()