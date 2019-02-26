import State

print "Running..."

state = State.State(debug=True)
state.ReportCreationTime()

state.DiscoverKnownDevices()

state.RegisterDeviceByName('CASIO USB-MIDI MIDI 1')
state.PrintRegisteredDevices()
state.PrintMidoPorts()
state.UnregisterDevice('CASIO USB-MIDI:CASIO USB-MIDI MIDI 1 24:0')
state.PrintRegisteredDevices()
state.PrintMidoPorts()

print "Finished"
