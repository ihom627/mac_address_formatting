# Copyright (c) 2015, RetailNext, Inc.
# This material contains trade secrets and confidential information of
# RetailNext, Inc.  Any use, reproduction, disclosure or dissemination
# is strictly prohibited without the explicit written permission
# of RetailNext, Inc.
# All rights reserved.
INVALID_MAC = -1

def convertMac(macInput, inputLength):

    print "inside convertMac()"
    print macInput
    print inputLength 
    temp = "foo"
    temp_int = 0
    result = 0
    count = 0 

    #if has :
    if ':' in macInput:
        temp = macInput.split(":")
        for element in reversed(temp):
            print "element %s " % element
            temp_int = int(element, 16)
            result += temp_int *  16 ** count    
            print result
            count += 2 

    #if has - 
    elif '-' in macInput:
        temp = macInput.split("-")
        for element in reversed(temp):
            print "element %s " % element
            temp_int = int(element, 16)
            result += temp_int *  16 ** count 
            print result
            count += 2

    # if has . and group by 4
    elif macInput.count('.') == 2:
        temp = macInput.split(".")
        for element in reversed(temp):
            print "element %s " % element
            temp_int = int(element, 16)
            result += temp_int *  16 ** count
            print result
            count += 4 


    # if has one - and group by 6 
    elif macInput.count('-') == 1:
        temp = macInput.split("-")
        for element in reversed(temp):
            print "element %s " % element
            temp_int = int(element, 16)
            result += temp_int *  16 ** count
            print result
            count += 6 

    #if has . and group by 2
    elif '.' in macInput:
        print "here in . and group by 2"
        temp = macInput.split(".")
        for element in reversed(temp):
            print "element %s " % element
            temp_int = int(element, 10)
            result += temp_int *  16 ** count
            print result
            count += 2


    # else no characters
    else:
        result = int(macInput, 16) 
        print result





    print "result = %x" % result
    print temp 
    return result



#    return INVALID_MAC

def main():
    testCases = [
        ["00:13:37:78:34:3E", 17, 0x00133778343E],
        ["00-13-37-78-34-3E", 17, 0x00133778343E],
        ["00:13:37:78:34:3e", 17, 0x00133778343E],
        ["0013.3778.343E", 14, 0x00133778343E],
        ["001337-78343E", 13, 0x00133778343E],
        ["00133778343e", 12, 0x00133778343E],
#        ["\x00\x13\x37\x78\x34\x3e", 6, 0x00133778343E],
        ["0:13:37:78:34:3e", 16, 0x00133778343E],
        ["0.19.55.120.52.62", 17, 0x00133778343E],

        ["0:1:3:7:3:3", 11, 0x000103070303],
        ["00:00:00:00:00:00", 17, 0x000000000000],
        ["FF:FF:FF:FF:FF:FF", 17, 0xFFFFFFFFFFFF],

        ["", 0, INVALID_MAC],
        ["fleshless-flinchingly", 21, INVALID_MAC],
        ["\x00\x11\x22\x33\x44\x55\x66", 7, INVALID_MAC],
        ["1.2.3.4.5.256", 13, INVALID_MAC],
        ["00:13:37:70:EA:86:", 18, INVALID_MAC],
        ["00112233445", 11, INVALID_MAC],
        ["aabbc-ddeeff", 12, INVALID_MAC]
    ]

    i = 0
    for case in testCases:
        i+=1
        convertedMac = convertMac(case[0], case[1])
        if convertedMac == case[2]:
            print "test %d: passed" % i
        else:
            print "test %d: failed!" % i
            print "         expected: %s but got: %s" % (case[2], convertedMac)

main()

