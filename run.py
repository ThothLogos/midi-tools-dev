import State

print "Running..."

state = State.State(debug=True)
state.ReportCreationTime()

state.DiscoverKnownDevices()

state.RegisterDeviceByName('CASIO USB-MIDI MIDI 1')

print "Finished"
