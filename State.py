import datetime
import mido
import re
import Device

EXCLUDED_DEVICES = ["ES1371 16", "Midi Through Port-0"]

class State:

    def __init__(self, debug=False):
        self.debug = debug
        self.createdAt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.discoveredDevices = []
        self.knownDevices = []
        self.registeredDevices = []
        self.currentKey = None
        self.currentBPM = None
        self.songPlaying = False
        self.currentSong = None

    def ReportCreationTime(self):
        print "State was created at: {}".format(self.createdAt)

    def DiscoverKnownDevices(self):
        self.discoveredDevices = mido.get_output_names()
        if len(self.discoveredDevices) > 0:
            self.SanitizeDiscoveredDevices(self.discoveredDevices)
            self.PrintDiscoveredDevices(self.discoveredDevices)
            self.RemoveExcludedDevices(self.discoveredDevices)
            self.PrintDiscoveredDevices(self.discoveredDevices)
        else:
            raise Exception("mido.get_output_names() returned no results")

    def SanitizeDiscoveredDevices(self, devices):
        if self.debug: print "Cleaning up raw device list..."
        for i in range(len(devices)):
            devices[i] = devices[i].split(":")[1]

    def RemoveExcludedDevices(self, devices):
        if self.debug: print "Cleaning up list of exlucded devices..."
        devices = set(devices) - set(EXCLUDED_DEVICES)

    def PrintDiscoveredDevices(self, devices):
        print "Discovered following raw devices:"
        for i in range(len(devices)):
            print "{} - {}".format(i, devices[i])

    def RegisterDeviceByName(self, name):
        if self.debug: print("Attempting to register name: {}".format(name))
        try:
            new_device = mido.open_output(name)
            self.registeredDevices.append(new_device)
        except Exception as e:
            print("ERROR: {}".format(e))

    def UnregisterDevice(self, name):
        if self.debug: print("Attempting to unregister name: {}".format(name))
        try:
            for i in range(len(self.registeredDevices)):
                if self.registeredDevices[i].name == name:
                    print("Found device {} - closing & unreg".format(name))
                    self.registeredDevices[i].close()
                    del(self.registeredDevices[i])
                else:
                    print("Unable to locate device: {}".format(name))
        except Exception as e:
            print("Failed to UnregisterDevice")
            print("ERROR: {}".format(e))

    def PrintRegisteredDevices(self):
        print "Currently Registered devices:"
        for i in range(len(self.registeredDevices)):
            print "{} - {}".format(i, self.registeredDevices[i])
        if not self.registeredDevices: print("RegDevices is empty!")

    def PrintMidoPorts(self):
        print(mido.get_output_names())


