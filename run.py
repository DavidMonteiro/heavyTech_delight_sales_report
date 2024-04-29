# Main python script

import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
import io_operations as io
import general_report as gen_report


sales = io.read_csv('heavyTech_delight_sales_2021.csv')



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
table_fig = gen_report.general_data_table(sales)
scatter_chart_fig = gen_report.general_bubble_chart(sales)
donut_chart_fig = gen_report.general_data_donutChart(sales)

#Push the table and the chart into the html string
html_content = push_to_html_report(html_content, table_fig)
html_content = push_to_html_report(html_content, scatter_chart_fig)
html_content = push_to_html_report(html_content, donut_chart_fig)


#Close the html page </body? & </html>
html_content = close_html_report(html_content)


#Generate html report in html format
io.generate_html_report("sales_report.html", html_content)