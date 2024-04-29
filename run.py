# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px

#Creating Sale dataframes from csv file > 'heavyTech_delight_sales_2021.csv'
try:
    sales = pd.read_csv('heavyTech_delight_sales_2021.csv')
except IOError as e:
     print('IO error: ' + e)



"""General functions for sales"""

"""function to count orders"""
def count_orders(df): 
    return df['Order_no'].count()

"""funcion to count hires"""
def count_rentals(df):  
    return (df['Finance_Type'] == 'rental').sum()

"""function to count capital purchase"""
def count_sales(df):  
    return (df['Finance_Type'] == 'sale').sum()

"""function to count products"""
def count_products(df):  
    return df['Product_Quantity'].sum()

"""function to count New Products""" 
def count_new_products(df): 
    return (df.loc[df['Product_State'] == 'new']).Product_Quantity.sum()

"""Function to count S/Hand Products"""
def count_refurbished_products(df):  
    return (df.loc[df['Product_State'] == 'refurbished']).Product_Quantity.sum()

"""Function to count no of unique companies"""
def count_companies(df):  
    return df['Company'].nunique()

"""Function to count no of unique counties"""
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

def general_data_table(df):
    """Function to generate table with sales data into an html file"""
    fig = go.Figure(data=[go.Table(header=dict(values=['Description:', 'Results']),
                    cells=dict(values=[
                        [
                            "Total Orders",
                            "Rentals",
                            "Sales",
                            "Total Products",
                            "New Products",
                            "Refurbished Products"
                        ], 
                        [
                            count_orders(df),
                            count_rentals(df),
                            count_sales(df),
                            count_products(df),
                            count_new_products(df),
                            count_refurbished_products(df)]]))
                        ])
    fig.update_layout(width=500)
    return fig.to_html(full_html=True, include_plotlyjs='cdn')

def general_data_donutChart(df):
    """Function to generate pie chart with sales data into an html file """
    data = df.groupby('Finance_Type')['Order_no'].count().reset_index()
    fig = px.pie(data, values='Order_no', names='Finance_Type', color = 'Finance_Type',
                    color_discrete_map = {'Sales': '#003f5c', 'Rentals': '#ffa600'})
    fig.update_traces(hole=.4, textinfo='value + percent',hovertemplate = "%{label}<br>Total Orders: %{value} </br>Percentage : %{percent}")
    return fig.to_html(full_html=True, include_plotlyjs='cdn')



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

def generate_html_report(html_filename0, html_block0):
    """Function generate and save a single HTML page"""
    file = open(html_filename0, "w") 
    file.write(html_block0)
    file.close()


#Start the html page as a string
html_content = start_html_report()

# Generate the table and the donut chart
table_fig = general_data_table(sales)
donut_chart_fig = general_data_donutChart(sales)

#Push the table and the chart into the html string
html_content = push_to_html_report(html_content, table_fig)
html_content = push_to_html_report(html_content, donut_chart_fig)


#Close the html page </body? & </html>
html_content = close_html_report(html_content)

#Generate html report in html format
generate_html_report("sales_report.html", html_content)