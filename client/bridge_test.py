from client import webBus
from operator import add
import testLib as t
import QIELib as q
b = webBus("pi5",0)

# Examlpe...
def bridge0(rm,slot):
    t.openRM(rm)
    b.write(q.QIEi2c[slot],[0x00])
    b.read(q.QIEi2c[slot],4)
    return b.sendBatch()[-1]

# Bridge Register Tests

def runBridgeTests(RMList, num_slots, num_tests, verbosity=0):
    total_passed = 0
    total_failed = 0
    total_neither = 0
    total_number_tests = num_slots * num_tests
    for rm in RMList:
        t.openRM(rm)
        for slot in xrange(num_slots):
            b.write(0x00,[0x06])
            test_list = basicTests(slot,num_tests)
	    return test_list


def basicTests(slot, num_tests, verbosity=0):
    resultStrings = []
    passed = 0
    failed = 0
    neither = 0
    for test in xrange(num_tests):
        function = bridgeDict[test]['function']
        address = bridgeDict[test]['address']
        num_bytes = bridgeDict[test]['bits']/8
        message = t.readRegister(slot, address, num_bytes)
	resultStrings.append(function(message))
    return resultStrings

##### TestLib ########

def passFail(result):
    if result:
        return 'PASS'
    return 'FAIL'

def idString(message):
    correct_value = "HERM"
    message = t.toASCII(message)
    #print 'correct value: ', correct_value
    #print 'ASCII message: ', message
    return message

def idStringCont(message):
    correct_value = "Brdg"
    message = t.toASCII(message)
    #print 'correct value: ', correct_value
    #print 'ASCII message: ', message
    return message

def fwVersion(message):
    # correct_value = "N/A" # We need to find Firmware Version
    message = t.toHex(message)
    return message

def ones(message):
    correct_value = '0xffffffff'
    hex_message = t.toHex(message,0)
    #print 'correct value: ', correct_value
    #print 'int message: ', message
    #print 'hex message: ', hex_message
    return hex_message

def zeroes(message):
    correct_value = '0x00000000'
    hex_message = t.toHex(message,0)
    return hex_message

def onesZeroes(message):
    correct_value = '0xaaaaaaaa'
    hex_message = t.toHex(message,0)
    #print 'correct value: ', correct_value
    #print 'int message: ', message
    #print 'hex message: ', hex_message
    return hex_message

# def qieDaisyChain0(messgae):
#     hex_message = t.toHex(message,1)
#     print 'int message: ', message
#     print 'hex message:', hex_message
#     qCard0 = q.qCard(b,0x30)
#     return hex_message
#
# def qieDaisyChain1(message):
#     hex_message = t.toHex(message,1)
#     print 'int message: ', message
#     print 'hex message:', hex_message
#     qCard1 = q.qCard(b,0x31)
#     return hex_message

def simplePrint(message):
    hex_message = t.toHex(message,1)
    #print 'int message: ', message
    #print 'hex message:', hex_message
    return hex_message

bridgeDict = {
    0 : {
        'name' : 'ID string',
        'function' : idString,
        'address' : 0x00,
        'bits' : 32,
        'write' : False
    },
    1 : {
        'name' : 'ID string cont',
        'function' : idStringCont,
        'address' : 0x01,
        'bits' : 32,
        'write' : False
    },
    2 : {
        'name' : 'FW Version',
        'function' : fwVersion,
        'address' : 0x04,
        'bits' : 32,
        'write' : False
    },
    3 : {
        'name' : 'Ones',
        'function' : ones,
        'address' : 0x08,
        'bits' : 32,
        'write' : False
    },
    4 : {
        'name' : 'Zeroes',
        'function' : zeroes,
        'address' : 0x09,
        'bits' : 32,
        'write' : False
    },
    5 : {
        'name' : 'OnesZeroes',
        'function' : onesZeroes,
        'address' : 0x0A,
        'bits' : 32,
        'write' : False
    },
    6 : {
        'name' : 'Scratch',
        # 'function' : scratch,
        'function' : simplePrint,
        'address' : 0x0B,
        'bits' : 32,
        'write' : True
    },
    7 : {
        'name' : 'Status',
        # 'function' : status,
        'function' : simplePrint,
        'address' : 0x10,
        'bits' : 32,
        'write' : False
    },
    8 : {
        'name' : 'I2C_SELECT',
        # 'function' : i2cSelect,
        'function' : simplePrint,
        'address' : 0x11,
        'bits' : 32, # 8 bits in documentation
        'write' : True
    },
    9 : {
        'name' : 'Clock Counter',
        # 'function' : clockCounter,
        'function' : simplePrint,
        'address' : 0x12,
        'bits' : 32,
        'write' : False
    },
    10 : {
        'name' : 'RES_QIE Counter',
        # 'function' : resQieCounter,
        'function' : simplePrint,
        'address' : 0x13,
        'bits' : 32,
        'write' : False
    },
    11 : {
        'name' : 'WTE Counter',
        # 'function' : wteCounter,
        'function' : simplePrint,
        'address' : 0x14,
        'bits' : 32,
        'write' : False
    },
    12 : {
        'name' : 'BkPln_Spare_1 Counter',
        # 'function' : bkPlnCounter1,
        'function' : simplePrint,
        'address' : 0x15,
        'bits' : 32,
        'write' : False
    },
    13 : {
        'name' : 'BkPln_Spare_2 Counter',
        # 'function' : bkPlnCounter2,
        'function' : simplePrint,
        'address' : 0x16,
        'bits' : 32,
        'write' : False
    },
    14 : {
        'name' : 'BkPln_Spare_3 Counter',
        # 'function' : bkPlnCounter3,
        'function' : simplePrint,
        'address' : 0x17,
        'bits' : 32,
        'write' : False
    },
    15 : {
        'name' : 'igloo2 FPGA Control',
        # 'function' : iglooControl,
        'function' : simplePrint,
        'address' : 0x22,
        'bits' : 11,
        'write' : True
    },
    16 : {
        'name' : 'ControlReg',
        # 'function' : controlReg,
        'function' : simplePrint,
        'address' : 0x2A,
        'bits' : 32,
        'write' : True
    },
    17 : {
        'name' : 'orbit_histo[167:144]',
        # 'function' : orbitHisto6,
        'function' : simplePrint,
        'address' : 0x2B,
        'bits' : 24,
        'write' : False
    },
    18 : {
        'name' : 'orbit_histo[143:120]',
        # 'function' : orbitHisto5,
        'function' : simplePrint,
        'address' : 0x2C,
        'bits' : 24,
        'write' : False
    },
    19 : {
        'name' : 'orbit_histo[119:96]',
        # 'function' : orbitHisto4,
        'function' : simplePrint,
        'address' : 0x2D,
        'bits' : 24,
        'write' : False
    },
    20 : {
        'name' : 'orbit_histo[95:72]',
        # 'function' : orbitHisto3,
        'function' : simplePrint,
        'address' : 0x2E,
        'bits' : 24,
        'write' : False
    },
    21 : {
        'name' : 'orbit_histo[71:48]',
        # 'function' : orbitHisto2,
        'function' : simplePrint,
        'address' : 0x2F,
        'bits' : 24,
        'write' : False
    },
    22 : {
        'name' : 'orbit_histo[47:24]',
        # 'function' : orbitHisto1,
        'function' : simplePrint,
        'address' : 0x30,
        'bits' : 24,
        'write' : False
    },
    23 : {
        'name' : 'orbit_histo[23:0]',
        # 'function' : orbitHisto0,
        'function' : simplePrint,
        'address' : 0x31,
        'bits' : 24,
        'write' : False
    },

    # QIE Daisy Chains. Chains 2 and 3 are not used.
    # Conflict between Orbits 0, 1 and Daisy Chains 0, 1.
    # Addresses 0x30, 0x31.
    24 : {
        'name' : 'QIE Daisy Chain 0',
        # 'function' : qieDaisyChain0,
        'function' : simplePrint,
        'address' : 0x30,
        'bits' : 384,
        'write' : True
    },
    25 : {
        'name' : 'QIE Daisy Chain 1',
        # 'function' : qieDaisyChain1,
        'function' : simplePrint,
        'address' : 0x31,
        'bits' : 384,
        'write' : True
    },
    26 : {
        'name' : 'Thermometer One Wire',
        # 'function' : thermOneWire,
        'function' : simplePrint,
        'address' : 0x40,
        'bits' : 32, # TBD in documentation
        'write' : True
    },
}
# I2C_SELECT Table (address 0x11)
i2cDict = {
    0 : {
        'name' : 'no select',
        # 'function' : noSelect,
        'function' : simplePrint,
        'value' : 0x00
    },
    1 : {
        'name' : 'VTTX 1 (Twin Transmitter)',
        # 'function' : vttx1,
        'function' : simplePrint,
        'value' : 0x01,
        'address' : 0x7E
    },
    2 : {
        'name' : 'VTTX 2 (Twin Transmitter)',
        # 'function' : vttx2,
        'function' : simplePrint,
        'value' : 0x02,
        'address' : 0x7E
    },
    3 : {
        'name' : 'igloo2 FPGA (unique FPGA for HE, Top for HB)',
        # 'function' : vttx1,
        'function' : simplePrint,
        'value' : 0x03,
        'address' : 0x09
    },
    4 : {
        'name' : 'DS28CM00 Silicon Serial Number (Unique ID)',
        # 'function' : uniqueID,
        'function' : simplePrint,
        'value' : 0x04,
        'address' : 0x50
    },
    5 : {
        'name' : 'SHT21 Humidity and Temperature Sensor',
        # 'function' : temp,
        'function' : simplePrint,
        'value' : 0x05,
        'address' : 0x40
    },
    7 : {
        'name' : 'igloo2 Bot_FPGA',
        # 'function' : temp,
        'function' : simplePrint,
        'value' : 0x07,
        'address' : 0x09
    }
}
