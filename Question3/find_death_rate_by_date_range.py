'''
find_death_rate_by_date_range.py
  Authour(s): Maximos Samuel (1184139)

  Project: CIS2250 W22 Project: COVID-19 Data Tracking
  Date of Last Update: Mar 22, 2022

    Functional Summary
      find_death_rate_by_date_range.py takes in a CSV file containing data
      regarding COVID-19 numbers (in this case, we will be using cases and deaths).
      The program will take a date range from the user and will use data from 
      the necessary data fields to calculate the amount of deaths that occur in that
      date range compared to the amount of new cases in the date range to calculate
      a death rate for each day.


    Commandline Parameters: 6
      argv[1] = Year of user's desired start date
      argv[2] = Month of user's desired start date
      argv[3] = Day of user's desired start date
      argv[4] = Year of user's desired end date
      argv[5] = Month of user's desired end date
      argv[6] = Day of user's desired end date


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
#fileSearch is a function that looks within the Question1 folder to find 
#the latest version of our needed data files. The function uses a while loop
#that goes through every file possibility from the end of 2022 until it finds
#the latest file in the directory
#

def fileSearch():
  
  for i in range (2022, 2020, -1):
    searchYear = i

    #Search by year
    
    for j in range (12, 0, -1):

      #Branch statements that modifies the string for file search
      
      if j < 10:
        searchMonth = "0" + str (j)
      else:
        searchMonth = str(j)

      #Search by day
      
      for k in range (31, 0, -1):
        if k < 10:
          searchDay = "0" + str (k)
        else:
          searchDay = str (k)

        #Search by last 2 numbers in file name

        for l in range (22, 24, 1):
          for m in range (1, 50, 1):
  
            if m < 10:
              fileValue = "0" + str(m)
            else:
              fileValue = str(m)
          
            fileName = f'Question3/covidtesting_{searchYear}-{searchMonth}-{searchDay}_{l}-{fileValue}.csv'
  
            try:
              test_file = open (fileName, encoding="utf-8-sig")
              return fileName
            except IOError as err:
              continue

  #Exit if no file is found
  print(f'Sorry. It appears no covidtesting file was found.')
  sys.exit(-1)
  
def main(argv):

  #
  #First checking if the command line was given a sufficient amount of parameters.
  #Program will then begin assigning command line arguments to better-named variables
  #
  
  if len(argv) != 7:
        print("Usage:",
                "python Question3/find_death_rate_by_date_range.py <start year> <start month> <start day> <end year> <end month> <end day>") 
        sys.exit(-1)
  
  startYear = argv[1]

  #
  #Next few if-else statements check if single digit arguments follow a '0', since
  #date.fromisoformat() does not work when a single digit parameter is not following
  #a '0', therefore, we format the strings appropriately
  #


  if int (argv[2]) < 10 and argv[2][0] != '0':
    startMonth = "0" + argv[2]
  else:
    startMonth = argv[2]
    
  if int (argv[3]) < 10 and argv[3][0] != '0':
    startDay = "0" + argv[3]
  else:
    startDay = argv[3]
  
  endYear = argv[4]
  
  if int (argv[5]) < 10 and argv[5][0] != '0': 
    endMonth = "0" + argv[5]
  else:
    endMonth = argv[5]
  
  if int (argv[6]) < 10 and argv[6][0] != '0':
    endDay = "0" + argv[6]
  else:
    endDay = argv[6]

  #Date strings are created then converted into date variables
  startDateString = f'{startYear}-{startMonth}-{startDay}'
  endDateString = f'{endYear}-{endMonth}-{endDay}'

  startDate = date.fromisoformat(startDateString)
  endDate = date.fromisoformat(endDateString)

  #Calling the fileSearch() function then opening the CSV file
  fileToOpen = fileSearch()
  fileName = open (fileToOpen, encoding="utf-8-sig")  
  fileReader = csv.reader(fileName)

  #Setting a firstLine variable to True so that the first line is skipped
  firstLine = True
  
  #Initializing currDaysCases and dayZeroDeaths to 0
  currDaysCases = 0
  currDaysDeaths = 0
  dayZeroDeaths = 0
  
  #For loop goes through every row in the data file
  for rowData in fileReader:

    #Skipping the first line and printing the first line of output
    if firstLine == True:
      print("Date,Death Rate (%)")
      firstLine = False
      continue
    
    #
    #If statement will check to see if the current row's date is the day
    #before the user's desired start date. If so, the variable dayZeroDeaths
    #is initialized to that day's number of deaths
    #
      
    if date.fromisoformat(rowData[0]) == startDate - timedelta(days = 1):
      
      #
      #First check to see if the date's deaths data field is empty, stays at 0
      #if so. If not, the variable is initialized to whatever is in the data field
      #
      
      if rowData[6] == '':
        dayZeroDeaths = 0
      else:
        dayZeroDeaths = int (rowData[6])

    #Program will check to see if the current row's date is within the user's date range.
    elif date.fromisoformat(rowData[0]) >= startDate and date.fromisoformat(rowData[0]) <= endDate:
      
      #
      #Check to see if deaths data field is empty. If so, the currDayDeaths is set to
      #0. CurrDayDeaths is the value which will be divided into the current day's cases
      #currDaysCases to get the current day's death rate (currDaysDeathRate)
      #
      
      if rowData[6] == '':
        currDaysDeaths += 0

        #Check to see if Confirmed Positive Data field is empty
        if rowData[4] == '':
          currDaysCases = 0
        else:
          currDaysCases += int (rowData[4])

        #Checking if currDaysCases is 0 to prevent division by zero error
        if currDaysCases == 0:
          currDaysDeathRate = 0
        else:
          currDaysDeathRate = (currDaysDeaths/currDaysCases) * 100

        #Printing current day's data
        print(f'{rowData[0]},{currDaysDeathRate}')
      else:
        #Check to see if Confirmed Positive Data field is empty
        if rowData[4] == '':
          currDaysCases = 0
        else:
          currDaysCases += int (rowData[4])
        

        #
        #CurrDaysDeaths is calculated by subtracting the deaths from dayZeroDeaths from
        #the current day's death
        #
        
        currDaysDeaths = int (rowData[6]) - dayZeroDeaths

        #Checking if currDaysCases is 0 to prevent division by zero error
        if currDaysCases == 0:
          currDaysDeathRate = 0
        else:
          #currDaysDeathRate is calculated by dividing currDaysDeaths by currDaysCases      
          currDayDeathRate = (currDaysDeaths/currDaysCases) * 100

        #printing of Data
        print(f'{rowData[0]},{currDayDeathRate}')

##
## Call our main function, passing the system argv as the parameter
##
        
main(sys.argv)

#
#End of script
#
