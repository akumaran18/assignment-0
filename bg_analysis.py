

#######################################
# Yao Li
# yaoli90@illinois.edu
# 2020.07.11
#######################################


import pandas
import numpy as np
import arrow
import matplotlib.pyplot as plt

################################################################################
## Step 1: Read data
#
# Your task is to load the average blood glucose for each member in each day
# into the matrix 'BG'.
# 1. Find all the unique member id
# 2. store average blood glucose in 'BG'
# - bg value in some date is missing. They will show as 'nan' in 'data'. You
#   need to replace the missing bg value as the average of the previous day
#   and the next day.
# - 'BG' has the size NUMBER_OF_MEMBERS X 365_DAYS. Store the bg value in the
#   matching date.

# read data from the csv file
data = pandas.read_csv('a.csv')

# store all the unique member id in 'member'
members = ###### Your Code Here ######
NUMBER_OF_MEMBERS = ###### Your Code Here ######

# initialize BG
BG = np.zeros((NUMBER_OF_MEMBERS,365))

# store bg value in BG

###### Your Code Here ######

# Handle the 'nan's in the data. Replace the nan with the previous non-nan value 
#or the next non-nan value. 

###### Your Code Here ######

################################################################################
## Step 1: Read data
#
# Usp the matplotlib to plot the averaged bg across all members ('avg_all')
# x-axis should be the 'date from first day (day)'
# y-axis shoule be 'bg'
# Add title as 'All member avg bg'

avg_all = np.average(BG, axis=0)

###### Your Code Here ######