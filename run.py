# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import pandas as pd

#Creating Sale dataframes from csv file > 'heavyTech_delight_sales_2021.csv'
try:
    sales = pd.read_csv('heavyTech_delight_sales_2021.csv')
except IOError as e:
     print('IO error: ' + e)



"""General functions for sales"""

#function to count orders
def count_orders(df):  
    return df['Order_no'].count()


#funcion to count hires
def count_rentals(df):  
    return (df['Finance_Type'] == 'rental').sum()


#function to count capital purchase
def count_sales(df):  
    return (df['Finance_Type'] == 'sale').sum()


#function to count products
def count_products(df):  
     return df['Product_Quantity'].sum()


#function to count New Products
def count_new_products(df):  
    return (df.loc[df['Product_State'] == 'New']).Product_Quantity.sum()


#Function to count S/Hand Products
def count_refurbished_products(df):  
    return (df.loc[df['Product_State'] == 'Refurbished']).Product_Quantity.sum()


#Function to count no of unique companies
def count_companies(df):  
    return df['Company'].nunique()


#Function to count no of unique counties/areas
def count_counties(df):  
    return df['County'].nunique()


print(count_orders(sales))
print(count_rentals(sales))
print(count_sales(sales))
print(count_products(sales))
print(count_new_products(sales))
print(count_refurbished_products(sales))
print(count_companies(sales))
print(count_counties(sales))