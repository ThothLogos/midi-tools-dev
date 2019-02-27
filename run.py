#!/usr/bin/python3

import State
import Device
import Helpers

state = State.State(debug=True)
state.ReportCreationTime()

#state.DiscoverKnownDevices()

#state.RegisterDeviceByName('CASIO USB-MIDI MIDI 1')
#state.PrintRegisteredDevices()
#state.PrintMidoPorts()
#state.UnregisterDevice('CASIO USB-MIDI:CASIO USB-MIDI MIDI 1 24:0')
#state.PrintRegisteredDevices()
#state.PrintMidoPorts()



newdev = Device.Device("TestDev", 11)
print("Dev channel: {}".format(newdev.channel))
newdev.SetChannel(13)
print("Dev channel: {}".format(newdev.channel))
newdev.SetChannel("16")
print("Dev channel: {}".format(newdev.channel))
