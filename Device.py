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
        if Helpers.IsValidChannel(int(channel)):
            self.channel = channel
        else: 
            print("Unable to modify device channel, not a number 0-15")
