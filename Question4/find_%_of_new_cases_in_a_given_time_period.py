'''
find_%_of_new_cases_in_a_given_time_period.py
  Authour(s): Maximos Samuel (1184139), Varun Kondam (1177900)

  Project: CIS2250 W22 Project: COVID-19 Data Tracking
  Date of Last Update: Mar 22, 2022

    Functional Summary
      find_%_of_new_cases_in_a_given_time_period.py is a program that reads
      data from multiple CSV files to determine what % of the province's covid
      cases in certain time range were from a specific region. Both the region
      and date range are up to the user. 

    Commandline Parameters: 9
      argv[1] = COVID Testing Data File
      argv[2] = PHU Data File
      argv[3] = Year of user's desired start date
      argv[4] = Month of user's desired start date
      argv[5] = Day of user's desired start date
      argv[6] = Year of user's desired end date
      argv[7] = Month of user's desired end date
      argv[8] = Day of user's desired end date
      argv[9] = User's desired PHU ID


    References
      Files containing school boards' active cases from https://ccodwg.github.io/Covid19CanadaArchive-data-explorer/
'''

#
#Packages and modules
#
import sys
import csv
from datetime import date, timedelta

#
#findDateInArray is a function used later in the program that searches for the
#index where a certain date is
#

def findDateInArray(array, desiredDate):
   
  #
  #indexValue is the value that will be returned if the desired school board
  #is found within the array
  #
  
  indexValue = 0

  #
  #For loop goes through every date in the array to see if it is the same the 
  #date. If so, the function returns the index containing that date,
  #if not, the indexValue increments
  #
  
  for i in array:
    if i[0] == desiredDate:
      return indexValue
    else:
      indexValue += 1
      continue
    
    #-1 is returned if the date isn't found in the array
    return -1

def main (argv):

  #
  #First checking if the command line was given a sufficient amount of parameters.
  #Program will then begin assigning command line arguments to better-named variables
  #
  
  if len(argv) != 10:
        print("Usage:",
                "python Question4/find_%_of_new_cases_in_a_given_time_period.py <covid testing data file> <PHU data file> <start year> <start month> <start day> <end year> <end month> <end day> <PHU ID>") 
        sys.exit(-1)
  
  startYear = argv[3]

  #
  #Next few if-else statements check if single digit arguments follow a '0', since
  #date.fromisoformat() does not work when a single digit parameter is not following
  #a '0', therefore, we format the strings appropriately
  #


  if int (argv[4]) < 10 and argv[4][0] != '0':
    startMonth = "0" + argv[4]
  else:
    startMonth = argv[4]
    
  if int (argv[5]) < 10 and argv[5][0] != '0':
    startDay = "0" + argv[5]
  else:
    startDay = argv[5]
  
  endYear = argv[6]
  
  if int (argv[7]) < 10 and argv[7][0] != '0': 
    endMonth = "0" + argv[7]
  else:
    endMonth = argv[7]
  
  if int (argv[8]) < 10 and argv[8][0] != '0':
    endDay = "0" + argv[8]
  else:
    endDay = argv[8]

  #Date strings are created then converted into date variables
  startDateString = f'{startYear}-{startMonth}-{startDay}'
  endDateString = f'{endYear}-{endMonth}-{endDay}'

  startDate = date.fromisoformat(startDateString)
  endDate = date.fromisoformat(endDateString)

  #Opening the needed data files

  testingFileName = argv[1]
  phuFileName = argv[2]
  phuNames = "Question4/PHU_IDs.csv"

  try:
    testingFile = open(testingFileName, encoding="utf-8-sig")
  except IOError as err:
    print("Unable to open names file '{}' : {}".format(testingFileName, err), file=sys.stderr)
    sys.exit(1)

  try:
    phuFile = open(phuFileName, encoding="utf-8-sig")
  except IOError as err:
    print("Unable to open names file '{}' : {}".format(phuFileName, err),file=sys.stderr)
    sys.exit(1)

  testingFileReader = csv.reader(testingFile)
  phuFileReader = csv.reader(phuFile)

  phuNamesFile = open(phuNames, encoding="utf-8-sig")
  phuNamesFileReader = csv.reader(phuNamesFile)

  phuID = argv[9]
  
  #initializing our data array
  dataArray = []

  #setting a firstLine boolean to true so we can skip over the first line
  firstLine = True

  #
  #First for loop goes through the PHU data file, adding elements to
  #dataArray if a row is within the date range and contains data for the
  #user's desired PHU
  #
  for rowData in phuFileReader:
    if firstLine == True:
      firstLine = False
      continue
      
    elif date.fromisoformat(rowData[0]) == startDate - timedelta(days=1) and rowData[2] == phuID:
     
      #
      #dayZeroCases will be subtracted from daily totals so as to calculate
      #the exact number of cases within the date range
      #
     
      dayZeroCases = int(rowData[3]) + int(rowData[4]) + int(rowData[5])

    elif date.fromisoformat(rowData[0]) >= startDate and date.fromisoformat(rowData[0]) <= endDate and rowData[2] == phuID:
      currDaysCases = (int(rowData[3]) + int(rowData[4]) + int(rowData[5])) - dayZeroCases
      dataArray.append([date.fromisoformat(rowData[0]), currDaysCases])

  firstLine = True

  #initializing totalCases to 0
  totalCases = 0

  #second for loop goes through testingFileReader
  for rowData in testingFileReader:
    if firstLine == True:
      firstLine = False
      continue

    #
    #if the row's date is within the date range, the program adds the
    #total amount of cases from startDate to the current date to said
    #date's element on the array
    #
      
    elif date.fromisoformat(rowData[0]) >= startDate and date.fromisoformat(rowData[0]) <= endDate:
      if rowData[4] == '':
        totalCases += 0
      else:
        totalCases += int(rowData[4])

      listIndex = findDateInArray(dataArray, date.fromisoformat(rowData[0]))

      if listIndex != -1:
        dataArray[listIndex].append(totalCases)

  #Getting the name of the user's desired PHU
  for rowData in phuNamesFileReader:
    if phuID == rowData[0]:
      desiredRegion = rowData[1]

  #printing first row
  print(f'Date, % of provincial cases reported by {desiredRegion}')

  #printing data
  for i in dataArray:
    print(f'{i[0]},{(int(i[1])/int(i[2])) * 100}')

main(sys.argv)
      
