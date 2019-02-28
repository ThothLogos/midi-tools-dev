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
newdev.SetChannel("8")
print("Dev channel: {}".format(newdev.channel))
newdev.SetChannel("02")
print("Dev channel: {}".format(newdev.channel))
newdev.SetChannel(0)
print("Dev channel: {}".format(newdev.channel))
newdev.SetChannel(3)
print("Dev channel: {}".format(newdev.channel))
newdev.SetChannel("0")
print("Dev channel: {}".format(newdev.channel))
newdev.SetChannel("9")
print("Dev channel: {}".format(newdev.channel))
newdev.SetChannel("000")
print("Dev channel: {}".format(newdev.channel))
newdev.SetChannel("21")
print("Dev channel: {}".format(newdev.channel))
newdev.SetChannel(33)
print("Dev channel: {}".format(newdev.channel))
newdev.SetChannel(newdev)
print("Dev channel: {}".format(newdev.channel))
