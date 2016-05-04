import asyncore, socket, sys

class AsyncUdpReceiver(asyncore.dispatcher):

    def __init__(self, host, port, rservo=None, lservo=None, **kwargs):
        asyncore.dispatcher.__init__(self)
        # open as udp socket
        self.create_socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.bind((host, port))

        self.rservo = rservo
        if rservo:
            self.rservo.start(0)

        self.lservo = lservo 
        if lservo:
            self.lservo.start(0)

        self.kp = kwargs.get('pk', 1)
        self.kd = kwargs.get('pd', 0.5)

        self.rpwr = 0
        self.lpwr = 0

    def handle_connect(self):
        pass

    def handle_close(self):
        self.close()

    def adjust_speeds(spds):

        # adjust for p-d control
        new_rpwr = float(spds[0])
        new_lpwr = float(spds[1])

        self.rpwr = self.kp * new_rpwr - self.kd * (new_rpwr - self.rpwr)
        self.lpwr = self.kp * new_lpwr - self.kd * (new_lpwr - self.lpwr)
        
        if self.rpwr > 100.0:
            self.rpwr = 100.0
        
        if self.lpwr > 100.0:
            self.lpwr = 100.0

    def handle_read(self):
        msg = self.recv(1024).split()
        print msg
        self.adjust_speeds((msg[0], msg[1]))
        self.rdir = msg[2]
        self.ldir = msg[3]
        if self.rservo and self.lservo:
            self.drive()

    def drive(self):
        self.rservo.set_direction(self.rdir)
        self.lservo.set_direction(self.ldir)
        self.rservo.set_spd(self.rpwr)
        self.lservo.set_spd(self.lpwr)
        print "driving {0}@{1}  {2}@{3}".format(
            self.rpwr, self.rdir, self.lpwr, self.ldir)


if __name__ == "__main__":

    server = AsyncUdpReceiver(sys.argv[1], 5000)
    print "Waiting for data..."
    asyncore.loop()