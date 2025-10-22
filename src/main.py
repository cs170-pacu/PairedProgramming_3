################################################################################
# File name:    main.py
# Author:       YOUR NAME HERE
# Date:         5/14/2025
# Class:        CS 170
# Assignment:   01Lab
# Purpose:      Demonstrate Codespaces & Python
# Hours:        1.5
################################################################################

import sys

# Files, Exceptions, Lists, Dictionaries
DELIMITER = ','
NAME = 0
VALUE = 1
dAssignments = {}
dStudents = {}

sFileName = input('Which file contains your data? ')

try:
    with open(sFileName) as fInputFile:
        lAssignmentInfo = fInputFile.readline().split(DELIMITER)

        for sAssignment in lAssignmentInfo:
            lAssignmentData = sAssignment.split()
            dAssignments[lAssignmentData[NAME]] = int(lAssignmentData[VALUE])

            print(f'Name: {lAssignmentData[NAME]} Max VALUE: {dAssignments[lAssignmentData[NAME]]}')

### WRITE PART TWO HERE

#### END PART TWO

### WRITE PART THREE HERE

#### END PART THREE
    print()
except Exception as err:
    print(err) # so you can see any errors if they occur!
    print(f'Cannot open file {sFileName}')
    sys.exit(-1)
