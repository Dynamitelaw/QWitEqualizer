import serial
import binascii
from random import randint
from time import sleep


BLUETOOTH_NAME = "QWIT-Equalizer"
BLUETOOTH_ADDR = "93:D3:61:FD:32:61"
BLUETOOTH_PORT = "COM8"

PACKETID_MIN = 34
PACKETID_MAX = 126

#Globals
g_PreviousBandGains = [0.001 for i in range(20)]

def gainToResistance(gain):
	'''
	Returns the two closest 8 bit integers (RA,RB) where RA/RB ~= gain
	''' 
	centerRes = 127
	deltaRes = (centerRes - centerRes*gain)/(gain + 1)
	RA = int(round(centerRes - deltaRes))
	RB = int(round(centerRes + deltaRes))

	return RA, RB


def bandIndexToAddress(index):
	'''
	'''
	#Determine which virtual bus the band belongs to
	subBus = 0
	if (index > 11):
		subBus = ord('A')
	elif (index > 3):
		subBus = ord('B')
	else:
		subBus = ord('C')

	#Determine AD5254 I2C address
	baseAddress = 44
	addressDeltas = {
		0 : 1,
		1 : 1,
		2 : 0,
		3 : 0,
		4 : 3,
		5 : 3,
		6 : 2,
		7 : 2,
		8 : 1,
		9 : 1,
		10 : 0,
		11 : 0,
		12 : 3,
		13 : 3,
		14 : 2,
		15 : 2,
		16 : 1,
		17 : 1,
		18 : 0,
		19 : 0
	}

	i2cAddress = baseAddress + addressDeltas.get(index)

	#Determine register addresses
	regA = 0
	regB = 0
	if (index%2 == 0):
		regA = 3
		regB = 2
	else:
		regA = 0
		regB = 1

	return subBus, i2cAddress, regA, regB
	

def sendPacket(packet, serialSocket):
	'''
	'''
	packetID = packet[0]
	packetBinary = bytes(packet)
	serialSocket.write(packetBinary)
	
	returnPacket = list(serialSocket.readline())
	if (packetID != returnPacket[0]):
			print("ERROR: Packet ID mismatch")

	return list(returnPacket)
	

def connectToEqualizer():
	'''
	'''
	serialSocket = serial.Serial(BLUETOOTH_PORT, 9600, timeout = 2)
	serialSocket.flushInput()

	return serialSocket


def updateBandSettings(index, gain, serialSocket):
	'''
	'''
	subBus, i2cAddress, regA, regB = bandIndexToAddress(index)
	RA, RB = gainToResistance(gain)

	#Create bt packet to update A
	packetID = randint(PACKETID_MIN, PACKETID_MAX)
	packet = [packetID, ord('S'), subBus, i2cAddress, regA, RA]
	resp = sendPacket(packet, serialSocket)

	#Create bt packet to update B
	packetID = randint(PACKETID_MIN, PACKETID_MAX)
	packet = [packetID, ord('S'), subBus, i2cAddress, regB, RB]
	resp = sendPacket(packet, serialSocket)


def updateEqualizer(bainGains):
	'''
	'''
	for i in range(20):
		newBandGain = bainGains[i]
		prevBandGain = g_PreviousBandGains[i]

		if (newBandGain != prevBandGain):
			g_PreviousBandGains[i] = newBandGain
			updateBandSettings(i, newBandGain, g_SerialSocket)


def getGains():
	'''
	'''
	gainsOut = []
	for index in range(20):
		#print("==================\nBand ", index)
		subBus, i2cAddress, regA, regB = bandIndexToAddress(index)
		#Create bt packet to get RA
		packetID = randint(PACKETID_MIN, PACKETID_MAX)
		#print(packetID)
		packet = [packetID, ord('G'), subBus, i2cAddress, regA]
		resp = sendPacket(packet, g_SerialSocket)
		RA = resp[2] - resp[3]

		#Create bt packet to get RB
		packetID = randint(PACKETID_MIN, PACKETID_MAX)
		#print(packetID)
		packet = [packetID, ord('G'), subBus, i2cAddress, regB]
		resp = sendPacket(packet, g_SerialSocket)
		RB = resp[2] - resp[3]		

		gain = (RA/RB)
		gainsOut.append(gain)

	return gainsOut


def resetEqualizerGains():
	'''
	'''
	updateEqualizer([1 for i in range(20)])

#Connect to equalizer
g_SerialSocket = connectToEqualizer()
