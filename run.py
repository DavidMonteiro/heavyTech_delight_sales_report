# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import pandas as pd

#Creating Sale dataframes from csv file > 'heavyTech_delight_sales_2021.csv'
try:
    sales = pd.read_csv('heavyTech_delight_sales_2021.csv')
except IOError as e:
     print('IO error: ' + e)

print(sales)