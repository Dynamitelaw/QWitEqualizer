import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.linear_model import LinearRegression 
from time import sleep


def exponentialToFloat(expString):
	'''
	Converts the exponential string into a float.
	'''
	eString = expString.split("e")
	return float(eString[0])*(10**float(eString[1]))


def decibalToGain(decibal):
	'''
	Convert decibal to gain
	'''
	return 10**(float(decibal)/20)


def gainToDecibal(gain):
	'''
	Convert gain to decibal
	'''
	gain = gain if (gain > 0) else abs(gain)
	return 20 * math.log10(gain)


def processRawData():
	'''
	Processes the raw data from spice simulations into correctly formatted csv files
	'''
	simulationDirectory = "../Spice/BodePlots/"
	simulationFiles = os.listdir(simulationDirectory)

	for fileName in simulationFiles:
		if (fileName != "ALL_NODES.csv"):
			file = open(simulationDirectory + fileName)
			outfileName = fileName
			if (fileName == "I_special.csv"):
				outfileName = "I.csv"
			
			ouptputFile = open("responseData/"+outfileName, "w")
			file.readline()  #skip first line of headers

			while (True):
				currentLine = file.readline().split("\t")
				if not(currentLine[0]):
					break

				outputline = ""
				frequency = exponentialToFloat(currentLine[0])
				outputline += str(frequency) + ","

				dataPoint = currentLine[1].replace("(", "").replace(")", "").split(",")	
				gainDbString = dataPoint[0].replace("dB", "")
				phaseString = dataPoint[1].replace("\r\n","")[:-1]

				gain = decibalToGain(exponentialToFloat(gainDbString))
				if (fileName == "I.csv"):
					gain = gain*1.11

				phase = exponentialToFloat(phaseString)

				outputline += str(gain) + "," + str(phase) + "\n"
				
				ouptputFile.write(outputline)

			file.close()
			ouptputFile.close()


def loadProccessedData(dictionary):
	'''
	Loads simulation data into a dictionary of pandas dataframes
	'''
	csvDirectory = "responseData/"
	csvFiles = os.listdir(csvDirectory)
	
	columns = ["Frequency", "Amplitude", "Phase"]

	bandNames = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
	for bandName in bandNames:
		fileName = bandName + ".csv"
		data = pd.read_csv(csvDirectory+fileName)
		data.columns = columns
		data.set_index("Frequency", inplace=True)
		dictionary[fileName.split(".")[0]] = data


bandResponseDictionary = {}
loadProccessedData(bandResponseDictionary)
def findFrequencyResponse(bandGains):
	'''
	Returns a dataframe containing the final output response based on the given band gains.
	'''
	columns = ["Frequency", "Gain"]
	netResponse = pd.DataFrame(columns = columns);
	frequencies = bandResponseDictionary["A"].index.values.tolist()
	
	for frequency in frequencies:
		dataPoints = []
		
		gainIndex = 0
		for bandName in bandResponseDictionary:
			if (bandName != "OUT"):
				bandGain = bandGains[gainIndex]
				bandData = bandResponseDictionary[bandName]
				dataPoints.append((bandGain*bandData.loc[frequency, "Amplitude"], bandData.loc[frequency, "Phase"]))
				gainIndex += 1
		anchorPhase = max(dataPoints)[1]

		totalAmplitude = 0
		for dataPoint in dataPoints:
			totalAmplitude += dataPoint[0]#*math.cos(math.radians(dataPoint[1] - anchorPhase))

		#gain = gainToDecibal(0.8*(1-math.exp(-5*totalAmplitude)) + (-0.30743047*totalAmplitude) + (0.77239751*(totalAmplitude**2)))
		gain = gainToDecibal(totalAmplitude)
		netResponse = netResponse.append({"Frequency" : frequency, "Gain" : gain}, ignore_index = True)
	
	netResponse.set_index("Frequency", inplace=True)
	
	return netResponse



#RGB Color Values
textColor = (230/255,219/255,116/255) #Sublime Text Yellow
facecolor=(39/255,40/255,34/255) #Sublime Dark Grey
graphcolor = (49/255,50/255,44/255) #Slightly lighter grey
axisColor = (200/255,200/255,200/255) #Mostly White
green = (76/255,255/255,0/255)
red = (255/255,20/255,0/255)

fig = plt.figure(facecolor=facecolor)
ax1 = fig.add_subplot(1,1,1)
axes = plt.gca()
def updateResponsePlot(responseData):
	ax1.clear()
	ax1.plot(responseData)

	#Color formatting
	ax1.spines['bottom'].set_color(axisColor)
	ax1.spines['top'].set_color(axisColor) 
	ax1.spines['right'].set_color(axisColor)
	ax1.spines['left'].set_color(axisColor)
	ax1.tick_params(axis='x', colors=axisColor)
	ax1.tick_params(axis='y', colors=axisColor)
	ax1.yaxis.label.set_color(axisColor)
	ax1.xaxis.label.set_color(axisColor) 
	ax1.set_facecolor(graphcolor)

	ax1.set_xscale('log')
	axes.set_ylim([-80, 80])
	axes.set_xlim([20, 20000])
	plt.xlabel("Frequency (Hz)")
	plt.ylabel("Gain (dB)")

plt.show(block = False) 
