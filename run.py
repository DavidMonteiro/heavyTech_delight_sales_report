# Main python script

import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
import io_operations as io

import general_report as gen_report
import order_report as ord_report
import product_report as prd_report

##ETL section - extract csv into dataframe and add two columns after making some adjustments
sales = io.read_csv('heavyTech_delight_sales_2021.csv')

# Change the format of column Date to type datetime
sales["Date"] = pd.to_datetime(sales["Date"], format="%Y-%m-%d")

# Create a new column for month and quarter
sales['Month'] = sales['Date'].dt.month_name()
sales['Quarter'] = sales['Date'].dt.quarter



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




#Start the html page as a string
html_content = start_html_report()

# Generate the table and the donut chart
html_content = gen_report.general_Analysis(sales, html_content)
html_content = ord_report.order_Analysis(sales, html_content)
html_content = prd_report.product_Analysis(sales, html_content)


#Close the html page </body? & </html>
html_content = close_html_report(html_content)


#Generate html report in html format
io.generate_html_report("sales_report.html", html_content)



