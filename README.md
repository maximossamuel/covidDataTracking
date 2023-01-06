# COVID-19 Data Tracking




## Getting Started
### Python
* Ensure you have the latest version of python installed


### Running the Program Setup
* Using your terminal navigate to the directory containing the folders Question1, Question2, Question3 and Question4


### Running the Program (Question 1)
* This program is meant to answer the question 'Which school boards in Ontario reported the highest amount of active COVID cases on a given day?'
* This program can be run by inputting the regular python run command, followed by the date you wish to get data for, followed by the name of the file you wish to write the data to
* For example, say we wish to get the data for December 16, 2020, we would input the following into the command line:
```
python Question1/find_top_reported_cases_by_school_board.py 2020 12 16 > Question1/Dec16.csv
```
* A CSV file should be output called Dec16.csv, now if we wish to make a bar graph showing the 20 school boards with the most active cases reported, we will input:
```
python Question1/create_school_board_bar_graph.py Question1/Dec16.csv Question1/Dec16.pdf
```
* This will create a document called Dec16.pdf, which contains the aforementioned bar graph


### Running the Program (Question 2)
* This program is meant to answer the question 'What is the percentage of each type of vaccine status in the ICU for each month in a given year?'
* This program can be run by inputting the regular python run command, followed by the cases and status files, the year and then the name of the file you wish to save to
* For example, if we wanted to get the data for the year 2021, we would input:
```
python Question2/find_percentage_of_ICU_cases.py Question2/Data/cases.csv Question2/Data/status.csv 2021 > Question2/data2021.csv
```
* A CSV file called data2021.csv should be created, use this data to get a line graph by inputting:
```
python Question2/plot_percentage_of_ICU_cases.py Question2/data2021.csv Question2/data2021.pdf
```
* This will create a document called data2021.pdf which contains the aforementioned line graph


### Running the Program (Question 3)
* This program is meant to answer the question 'What is the provincial death rate of COVID during a given date range?'
* How this program works is that if you input December 1st to December 8th for example, what the program will do is it will calculate the death rate using how many deaths and cases occured on December 1st. Then for December 2nd, it'll calculate the death rate using how many deaths and cases occured in December 2nd and so on and so forth. 
* This program is run by inputting the regular python run command, followed by the start date, end date, followed by the name of the new file you wish to use.
* For example, if we wanted to get data from April 1st to April 30th of 2021, we input:
```
python Question3/find_death_rate_by_date_range.py 2021 4 1 2021 4 30 > Question3/April2021.csv
```
* This should create a CSV called April2021.csv, if we wish to make a line grapb out of that CSV, we input:
```
python Question3/create_death_rate_plot.py Question3/April2021.csv Question3/April2021.pdf
```
* This should create April2021.pdf, which contains the aforementioned line graph


### Running the Program (Question 4)
* This program is meant to answer the question 'A given region makes up for what % of new provincial cases within a certain time period?'
* This program is run by inputting the regular python run command, followed by the start date, end date, the PHU id for the desired region and the desired name of the output file
* Also note that all PHU IDs can be found in Question4/PHU_IDs.csv
* For example, if we wish to get the numbers for Ottawa from January to April of 2021, we would input:
```
python Question4/find_%_of_new_cases_in_a_given_time_period.py Question4/covidtesting.csv Question4/cases_by_status_and_phu.csv 2021 1 1 2021 5 1 2251 > Question4/Ottawa.csv
```
* A CSV file called Ottawa.csv should be output. If we wish to get a line graph for this data, we input:
```
python Question4/create_percentage_plot.py Question4/Ottawa.csv Question4/Ottawa.pdf
```
* This should create Ottawa.pdf, which contains the aforementioned line graph



## About the Authors

Maximos Samuel maximos@uoguelph.ca
Nathan Starkman
Varun Kondam
