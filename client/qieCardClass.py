# qieCardClass.py
#
# This is a class that will contain basic information
# about an individual QIE Card along with how it fared
# on the tests that it was subjected to.
#
# Created on June 10 2016

class qieCard:
	def __init__(self):
		# Create variables to store information 
	
		# Test parameters/info
		self.timeOfTest = ""
		self.tester     = ""
		
		# Data from card
		self.i2cAddress  = ""
		self.uniqueID    = ""
		self.temperature = -999.99
		self.humidity    = -999.99
		self.firmwareVer = ""
		self.vttx1Result = ""
		self.vttx2Result = ""

		# Test results
		self.passedTemp  = False
		self.passedHumid = False
		self.passedHerm  = False
		self.passedBrdg  = False
		self.passedOnes  = False
		self.passedZero  = False

		# Results from Caleb/Jordan's bridge tests
		self.thermOneWire = ""
		self.qieDaisyChn0 = ""
		self.qieDaisyChn1 = ""
		self.orbitHisto6  = "" 
		self.orbitHisto5  = ""
		self.orbitHisto4  = ""
		self.orbitHisto3  = ""
		self.orbitHisto2  = ""
		self.orbitHisto1  = ""		
		self.orbitHisto0  = ""
		self.controlReg   = ""
		self.igloo2Cntrl  = ""
		self.bkplnSpare3Counter = ""
		self.bkplnSpare2Counter = ""
		self.bkplnSpare1Counter = ""
		self.wteCounter = ""
		self.resQieCounter = ""
		self.clockCounter = ""
		self.scratch = ""
		self.onesZeros = ""




