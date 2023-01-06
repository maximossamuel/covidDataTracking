'''
find_top_reported_cases_by_school_board.py
  Authour(s): Maximos Samuel (1184139)

  Project: CIS2250 W22 Project: COVID-19 Data Tracking
  Date of Last Update: Mar 22, 2022

    Functional Summary
      find_top_reported_cases_by_school_board.py reads a CSV file and will
      calculate how many active COVID-19 cases have been reported by school boards
      across Ontario on a day that the user inputs into the command line. The
      program will then print a list of all the school boards that have reported
      cases that day along with how many cases they reported to standard output.

    Commandline Parameters: 3
      argv[1] = Year of user's desired date
      argv[2] = Month of user's desired date
      argv[3] = Day of user's desired date

    References
      Files containing school boards' active cases from https://ccodwg.github.io/Covid19CanadaArchive-data-explorer/
'''

#
#Packages and modules
#

import sys
import csv
from datetime import date

#
#fileSearch is a function that looks within the Question1 folder to find 
#the latest version of our needed data files. The function uses a while loop
#that goes through every file possibility from the end of 2022 until it finds
#the latest file in the directory
#

def fileSearch(fileString):

  #Search by year
  
  for i in range (2022, 2019, -1):
    searchYear = i

    #Search by month
    
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
          
            fileName = f'Question1/{fileString}_{searchYear}-{searchMonth}-{searchDay}_{l}-{fileValue}.csv'
  
            try:
              test_file = open (fileName, encoding="utf-8-sig")
              return fileName
            except IOError as err:
              continue

  #Exit if no file was found
  print(f'Sorry. It appears no {fileString} file was found.')
  sys.exit(-1)
  
#
#searchArray is a function used later in the program that checks if a certain
#school board is already in the array of school boards. 
#
              
def searchArray(array, schoolBoard):
  
  #
  #indexValue is the value that will be returned if the desired school board
  #is found within the array
  #
  
  indexValue = 0

  #
  #For loop goes through every school board in the array to see if it is the same the 
  #desired school board. If so, the function returns the index containing that school,
  #if not, the indexValue increments
  #
  
  for i in array:
    if i[0] == schoolBoard:
      return indexValue
    else:
      indexValue += 1
      continue

  #
  #The function will return -1 if it reaches the end of the loop and the school board 
  #is not found
  #
      
  return -1


  
def main(argv):

  #
  #First checking if the command line was given a sufficient amount of parameters.
  #Program will then begin assigning command line arguments to better-named variables
  #
  
  if len(argv) != 4:
    print("Usage:",
                "python Question1/find_top_reported_cases_by_school_board.py <year> <month> <day>") 
    sys.exit(-1)
  
  userYear = argv[1]

  #
  #Next few if-else statements check if single digit arguments follow a '0', since
  #date.fromisoformat() does not work when a single digit parameter is not following
  #a '0', therefore, we format the strings appropriately
  #

  if int (argv[2]) < 10 and argv[2][0] != '0':
    userMonth = "0" + argv[2]
  else:
    userMonth = argv[2]
    
  if int (argv[3]) < 10 and argv[3][0] != '0':
    userDay = "0" + argv[3]
  else:
    userDay = argv[3]

  #A date string is created, then converted to a date variable

  dateString = f'{userYear}-{userMonth}-{userDay}'

  userDate = date.fromisoformat(dateString)

  #
  #Due to the nature of how our required data files were updated, the fileSearch
  #function is ran twice.
  #

  oldFileOpen = fileSearch("schoolsactivecovid")
  oldFileName = open(oldFileOpen, encoding="utf-8-sig")
  oldFileReader = csv.reader(oldFileName)
  
  recentFileOpen = fileSearch("schoolrecentcovid2021_2022")
  recentFileName = open (recentFileOpen, encoding="utf-8-sig")  
  recentFileReader = csv.reader(recentFileName)

  #Setting a firstLine variable to True so that the first line is skipped
  firstLine = True

  #Declaring the array where the school boards and their cases are stored
  schoolBoardArray = []


  #For loop goes through every row in both data files.
  for rowData in oldFileReader:

    #Skipping the first line
    if firstLine == True:
      firstLine = False
      continue

    #
    #Checking to see if the current row's date is the same as the user's
    #desired date. If so, the searchArray function is ran to see if the row's 
    #school board is already in the array. If so, the loop simply adds the row's
    #number of active cases to cumulative active cases of the school board. If not,
    #the school board and the current number of active cases is appended.
    #
      
    if date.fromisoformat(rowData[1]) == userDate:
      schoolBoardFound = searchArray(schoolBoardArray, rowData[2])
      if schoolBoardFound != -1:
        schoolBoardArray[schoolBoardFound][1] += int(rowData[9])
      else:
        schoolBoardArray.append([rowData[2],int(rowData[9])])

  #Setting a firstLine variable to True so that the first line is skipped
  firstLine = True

  #For loop goes through every row in data file.
  for rowData in recentFileReader:

    #Skipping the first line
    if firstLine == True:
      firstLine = False
      continue

    #
    #Checking to see if the current row's date is the same as the user's
    #desired date. If so, the searchArray function is ran to see if the row's 
    #school board is already in the array. If so, the loop simply adds the row's
    #number of active cases to cumulative active cases of the school board. If not,
    #the school board and the current number of active cases is appended.
    #
      
    if date.fromisoformat(rowData[1]) == userDate:
      schoolBoardFound = searchArray(schoolBoardArray, rowData[2])
      if schoolBoardFound != -1:
        schoolBoardArray[schoolBoardFound][1] += int(rowData[9])
      else:
        schoolBoardArray.append([rowData[2],int(rowData[9])])

  #
  #Checking to see if there is nothing in schoolBoardArray, meaning no cases were
  #recorded on the user's desired date
  #
        
  if len(schoolBoardArray) == 0:
    print("Sorry, no cases were reported that day. It would seem you put in a day where schools weren't in session and/or cases weren't being recorded")
    sys.exit(-1)
  
  #If data is found, the array is sorted by highest amount of active cases
  else:
    schoolBoardArray.sort(key = lambda schoolBoardArray: schoolBoardArray[1], reverse=True)

    #
    #A new array is made. This array will contain the 20 (or less) school boards
    #with the highest number of active cases. 
    #
    
    displayArray = []

    for i in range (0, 20, 1):
      #For loop will end if there is less than 20 school boards in the array 
      if i == len(schoolBoardArray):
        break
      else:
        displayArray.append(schoolBoardArray[i])

    #The new array is then sorted by alphabetical order
    displayArray.sort()

    #Printing first line of output
    print(f'School Board,Number of Active Cases on {userDate}')

    #For loop then prints every element in the new array
    for i in displayArray:
      print(f'{i[0]},{i[1]}')

##
## Call our main function, passing the system argv as the parameter
##
      
main(sys.argv)

#
#End of script
#