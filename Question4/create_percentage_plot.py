#!/usr/bin/env python

'''
create_percentage_plot.py
(Previously create_death_rate_plot.py)
  Author(s): Maximos Samuel (1184139)
  Earlier contributors(s): Nathan Starkman (1127811), Varun Kondam (1177900), Andrew Hamilton-Wright, Kassy Raymond

  Project: CIS2250 W22 Project: COVID-19 Data Tracking
  Date of Last Update: Mar 22, 2022.

  Functional Summary
      create_percentage_plot.py reads a CSV file and saves
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
from matplotlib import ticker as ticktools

def main(argv):

  #
  #   Checking if the right number of parameters were given and assigning
  #   them to better-named variable
  #
  if len(argv) != 3:
      print("Usage:","python Question4/create_percentage_plot.py <data file> <graphics file> ")
      sys.exit(-1)

  csv_filename = argv[1]
  graphics_filename = argv[2]


  #
  # Open the data file using "pandas", which will attempt to read
  # in the entire CSV file
  #
  try:
      csv_df = pd.read_csv(csv_filename)
      datafile_alt = open(csv_filename)
  
  except IOError as err:
    print("Unable to open source file", csv_filename,": {}".format(err), file=sys.stderr)
    sys.exit(-1)


  #
  #Next, the datafile is opened again so we can get the name of the
  #user's desired PHU and insert it into the graph.
  #

  datafile_alt_reader = csv.reader(datafile_alt)

  for rowData in datafile_alt_reader:
    desiredYAxisString = rowData[1]
    break

  # At this point in the file, we begin to do the plotting

  fig = plt.figure()

  # Using seaborn to create a lineplot
  ax = sns.lineplot(x = "Date", y = desiredYAxisString, data=csv_df)

  #sets number of axis labels to 6
  ax.xaxis.set_major_locator(ticktools.MaxNLocator(6))

  #Rotate the ticks on the x-axis by 45 degrees
  plt.xticks(rotation = 45, ha = 'right')


  # Saving figure to a file
  fig.savefig(graphics_filename, bbox_inches="tight")

  #
  #   End of Function
  #



##
## Call our main function, passing the system argv as the parameter
##
main(sys.argv)

#
#   End of Script
#
