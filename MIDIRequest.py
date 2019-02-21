# MIDIRequest module
import MIDINoteDict
import pprint

def ScaleMajorAscending(fundamental, cycles=1, octaves=1, skip_pos=[]):
	print("REQ: ScaleMajorAscending - fundamental: {} cycles: {}, octaves: {},"
		" skip_pos: {}").format(fundamental, str(cycles), str(octaves), str(skip_pos))
	#notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
	notes = []
	for i in range(cycles):
		print "\tNotes: {}".format(notes)

def PrintRequest(type, args=[]):
	print "REQ {}: ".format(type)

def PlayMIDIFile(filename, dir="./"):
	print "TODO: PlayMIDIFile"

def PrintNoteDict():
	#pprint.pprint(MIDINoteDict.note_map)
	print MIDINoteDict.note_map
