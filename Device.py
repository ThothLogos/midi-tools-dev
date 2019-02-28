import Helpers

class Device(object):

    def __init__(self, name, channel):
        self.name = name
        self.channel = Helpers.EnsureInteger(channel)
        self.discovered = True
        self.known = False
        self.registered = False

    def SetKnown(self):
        self.known = True

    def SetRegistered(self):
        self.registered = True

    def Unregister(self):
        self.registered = False

    def SetChannel(self, channel):
        channel_int = Helpers.EnsureInteger(channel)
        if Helpers.IsValidChannel(channel_int):
            self.channel = channel_int
        else: 
            #raise Exception("SetChannel requires value 0-15, passed {}".format(channel))
            print("SetChannel requires value 0-15, passed {}".format(channel_int))
