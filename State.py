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
