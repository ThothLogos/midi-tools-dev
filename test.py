import mido
import MIDIRequest
import time

def GetOutputDeviceNameByID(id):
	devices = mido.get_output_names()
	if len(devices) > 0:
		print "Selecting device by ID: {}, Device Name: {}".format(id, devices[id])
		return devices[id]
	else:
		print "No devices found."
		return None	

def PrintOutputDevices():
	devices = mido.get_output_names()
	print "Connected Output Devices:"
	for i in range(len(devices)):
		print "{} - {}".format(i, devices[i])

def CreatePortByDeviceName(name):
	try:
		port = mido.open_output(name)
		return port
	except IOError as e:
		print "Port Error: {}".format(e)

MIDIRequest.ScaleMajorAscending("C")

MIDIRequest.PrintNoteDict()











#device_name = GetOutputDeviceNameByID(0)
#port = CreatePortByDeviceName(device_name)










'''
PrintOutputDevices()



print("Selected Device: {}").format(device_name)


port.reset()
print("Small delay...")
time.sleep(1)

msg = mido.Message('note_on', channel=0, note=60)
msg_off = mido.Message('note_off', channel=0, note=60)
msg2 = mido.Message('note_on', channel=0, note=65)
msg2_off = mido.Message('note_off', channel=0, note=65)

print("Sending MSG: {}").format(str(msg))
port.send(msg)
time.sleep(1)
print("Sending MSG: {}").format(str(msg_off))
port.send(msg_off)
time.sleep(0.5)

print("Sending MSG: {}").format(str(msg2))
port.send(msg2)
time.sleep(1)
print("Sending MSG: {}").format(str(msg2_off))
port.send(msg2_off)

for msg in mido.MidiFile('deb_clai_format0.mid').play():
	print(str(msg))
	port.send(msg)

port.reset()
time.sleep(1)
port.close()
'''