'''
create_school_board_bar_graph.py
(Previously create_ON_phu_cases_plot.py)
  Author(s): Maximos Samuel (1184139)
  Earlier contributors(s): Nathan Starkman (1127811), Varun Kondam (1177900), Andrew Hamilton-Wright, Kassy Raymond

  Project: CIS2250 W22 Project: COVID-19 Data Tracking
  Date of Last Update: Mar 29, 2022.

  Functional Summary
      create_ON_phu_cases_plot.py reads a CSV file and saves
      a plot based on the data to a PDF file.

     Commandline Parameters: 2
        sys.argv[0] = name of file to read
        sys.argv[1] = name of graphics file to create
'''

#
#   Packages and modules
#
import sys
import csv
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

def main(argv):

  #
  #   Checking if the right number of parameters were given and assigning
  #   them to better-named variable
  #
  
  if len(argv) != 3:
    print("Usage: python Question1/create_school_board_bar_graph.py <data file> <graphics file>")
    sys.exit(-1)

  dataFileName = argv[1]
  graphicsFileName = argv[2]

  #
  # Open the data file using "pandas", which will attempt to read
  # in the entire CSV file
  #
  
  try:
    dataFile = pd.read_csv(dataFileName)
    dataFileAlt = open(dataFileName)
  except IOError as err:
        print("Unable to open source file", dataFileName,": {}".format(err), file=sys.stderr)

  #
  #Next, the datafile is opened again so we can get the name of the
  #user's desired PHU and insert it into the graph.
  #

  dataFileAltReader = csv.reader(dataFileAlt)

  for rowData in dataFileAltReader:
    desiredXAxisString = rowData[1]
    break


  # At this point in the file, we begin to do the plotting

  fig = plt.figure()

  # Using seaborn to create a barplot
  
  ax = sns.barplot(x = desiredXAxisString, y = "School Board", data=dataFile, color="blue", dodge=False)

  # Saving figure to a file
  
  fig.savefig(graphicsFileName, bbox_inches="tight")

##
## Call our main function, passing the system argv as the parameter
##
  
main(sys.argv)

#
#End of script
#