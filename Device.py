class Device:

    def __init__(self, name, channel):
        self.name = name
        self.channel = channel
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
        if int(channel): 
            self.channel = channel
        else: 
            print("Unable to modify device channel, not a number")
