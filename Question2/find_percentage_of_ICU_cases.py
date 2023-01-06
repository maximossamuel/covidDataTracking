  #!/usr/bin/env python
  #python Question2/question2.py Question2/cases.csv Question2/status.csv 2022
'''
find_percentage_of_ICU_cases.py
  Author(s): Nathan Starkman
  Project: Group Assignment Script Plot
  Date of Last Update: March 24, 2022.

  Functional Summary
      find_percentage_of_ICU_cases.py finds the percentage of each type of vaccine status and gives the percentage of that case in the ICU for each month in a given year

     Commandline Parameters: 2
        sys.argv[0] = File with ICU data
        sys.argv[1] = File with overall data
        sys.argv[2] = The year of data you wish to print
'''
import sys


import csv

from datetime import date



def main(argv):

    if len(argv) != 4:
       print("Usage:",
               "create_name_plot.py <data file> <graphics file>")
       sys.exit(-1)
    
    fileName = argv[1]
    fileName2 = argv[2]
    inputYear = int(argv[3])
  

    try:
            file_name_fh = open(fileName, encoding="utf-8-sig")
    except IOError as err:
            print("Unable to open names file '{}' : {}".format(
                fileName, err),
                  file=sys.stderr)
            sys.exit(1)

    try:
            file_name2_fh = open(fileName2, encoding="utf-8-sig")
    except IOError as err:
            print("Unable to open names file '{}' : {}".format(fileName2, err),
                  file=sys.stderr)
            sys.exit(1)



    ICUyear = 0
    year = 0
    ICUmonth = 0
    month = 0
    TotalUnvacArray = [];
    TotalVacArray = [];
    TotalPartvacArray = [];
    TotalICUUnvacArray = [];
    TotalICUVacArray = [];
    TotalICUPartvacArray = [];
    
    for i in range (1, 13, 1):
      file_name_fh = open(fileName, encoding="utf-8-sig")

      file_namedata_reader = csv.reader(file_name_fh)
      file_name2_fh = open(fileName2, encoding="utf-8-sig")

      file_name2data_reader = csv.reader(file_name2_fh)
      totalUnvac = 0
      totalPvac = 0
      totalFvac = 0
      
      totalICUUnvac = 0
      totalICUPvac = 0
      totalICUFvac = 0
      
      firstLine = True
      for row_data_fields2 in file_name2data_reader:
        if firstLine == True:
          #print(','.join(row_data_fields2))
          firstLine =False
          continue
        ICUcurrDate = date.fromisoformat(row_data_fields2[0])
        
        ICUunVacNum = row_data_fields2[1]
        ICUpartialVacNum = row_data_fields2[2]
        ICUfullVacNum = row_data_fields2[3]

        if ICUcurrDate.month == i:
          totalICUUnvac+= int (ICUunVacNum)
          totalICUPvac+=int (ICUpartialVacNum)
          totalICUFvac+= int (ICUfullVacNum)
          ICUmonth = ICUcurrDate.month
          ICUyear = ICUcurrDate.year
      if ICUyear == inputYear:
        if totalICUUnvac !=0 or totalICUPvac !=0 or totalICUFvac !=0:
          TotalICUUnvacArray.append([ ICUmonth, totalICUUnvac]) 
          TotalICUPartvacArray.append([ICUmonth, totalICUPvac])
          TotalICUVacArray.append([ ICUmonth, totalICUFvac])

      
      firstLine = True
      for row_data_fields in file_namedata_reader:
        if firstLine == True:
          firstLine =False
          continue
        currDate = date.fromisoformat(row_data_fields[0])
        
        unVacNum = row_data_fields[1]
        partialVacNum = row_data_fields[2]
        fullVacNum = row_data_fields[3]

        x = i
        if currDate.month == x:
          totalUnvac += int (unVacNum)
          totalFvac += int(fullVacNum)
          totalPvac += int(partialVacNum)
          month = currDate.month
          year = currDate.year
      if year == inputYear:
        if (totalUnvac !=0) or (totalPvac !=0) or (totalFvac!=0):
          TotalUnvacArray.append([month, totalUnvac])
          TotalPartvacArray.append([month, totalPvac])
          TotalVacArray.append([ month, totalFvac])
     

    
    print("Month,Unvaccinated_Percentage,Partially_Vaccinated_Percentage,Fully_Vaccinated_Percentage")
    for x in range (len(TotalICUUnvacArray)):
      
      for y in range (len(TotalICUUnvacArray[x])):
         if y == 1:

          TotalUnvacArray[x][y]=round((TotalICUUnvacArray[x][y]/TotalUnvacArray[x][y])*100, 3)
          TotalPartvacArray[x][y] = round((TotalICUPartvacArray[x][y]/TotalPartvacArray[x][y])*100, 3) 
          TotalVacArray[x][y] = round((TotalICUVacArray[x][y]/TotalVacArray[x][y])*100, 3)

      if (TotalUnvacArray[x][0] == 1):
          wordMonth = "January"
      if (TotalUnvacArray[x][0] == 2):
          wordMonth = "Febuary"
      if (TotalUnvacArray[x][0] == 3):
          wordMonth = "March"
      if (TotalUnvacArray[x][0] == 4):
          wordMonth = "April"
      if (TotalUnvacArray[x][0] == 5):
          wordMonth = "May"
      if (TotalUnvacArray[x][0] == 6):
          wordMonth = "June"
      if (TotalUnvacArray[x][0] == 7):
          wordMonth = "July"
      if (TotalUnvacArray[x][0] == 8):
          wordMonth = "August"
      if (TotalUnvacArray[x][0] == 9):
          wordMonth = "September"
      if (TotalUnvacArray[x][0] == 10):
          wordMonth = "October"
      if (TotalUnvacArray[x][0] == 11):
          wordMonth = "November"
      if (TotalUnvacArray[x][0] == 12):
          wordMonth = "December"
      print("{},{},{},{}".format(wordMonth,TotalUnvacArray[x][1],TotalPartvacArray[x][1],TotalVacArray[x][1]))
       



main(sys.argv)


#
#  End of Script
#


