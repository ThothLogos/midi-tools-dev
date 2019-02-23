import State

print "Running..."

state = State.State(debug=True)
state.ReportCreationTime()

state.DiscoverKnownDevices()

print "Finished"
