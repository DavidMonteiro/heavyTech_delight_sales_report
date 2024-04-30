# Main python script

import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
import io_operations as io

import general_report as gen_report
import order_report as ord_report
import product_report as prd_report
import report_generator as generator
import csv_generator as myCSV


#def upload_sales_data():
#   #User gets to upload his own sales data
#   file_path = input("Please enter the path to the CSV file you want to upload: \n")
#
#   # Check if the file exists
#   if os.path.exists(file_path):
#       generate_report(file_path)
#   else:
#       print("File not found!")


def start_html_report():
    """Function to start a single HTML page"""
    html_content0 = "<html>\n"
    html_content0 += "<head>\n"
    html_content0 += "<title>Sales Data</title>\n"
    html_content0 += "</head>\n"
    html_content0 += "<body>\n"

    return html_content0

def push_to_html_report(html_content0, html_block0):
    """Function to add a single HTML section to the HTML page"""
    html_content0 += html_block0
    html_content0 += "\n"
    return html_content0

def close_html_report(html_content0):
    """Function to close the HTML page"""
    html_content0 += "</body>\n"
    html_content0 += "</html>\n"
    return html_content0


def generate_report(filename):

    ##ETL section - extract csv into dataframe and add two columns after making some adjustments
    sales = io.read_csv('heavyTech_delight_sales_2021.csv')

    # Change the format of column Date to type datetime
    sales["Date"] = pd.to_datetime(sales["Date"], format="%Y-%m-%d")

    # Create a new column for month and quarter
    sales['Month'] = sales['Date'].dt.month_name()
    sales['Quarter'] = sales['Date'].dt.quarter

    #Start the html page as a string
    html_content = start_html_report()

    ## Generate the Analysis
    html_content += generator.completeAnalysis(sales)


    #Close the html page </body? & </html>
    html_content = close_html_report(html_content)


    #Generate html report in html format
    io.generate_html_report("sales_report.html", html_content)


def run_Main():
    print("Hi! This is the Report Generator for Sales of Heavy Machinery!")
    choice = input("Do you want to use a mock CSV (enter '1') or upload your own CSV (enter '2')? \n")

    if choice.lower() == '1':
        myCSV.generate_sales_data(200)
        generate_report('heavyTech_delight_sales_2021.csv')
        
    elif choice.lower() == '2':
        #upload_sales_data()
        print("Oops.. This is still in construction")
    else:
        #I am calling the function itself making it recursive
        print("Invalid choice. Please enter '1' or '2'.")
        run_Main()

run_Main()

