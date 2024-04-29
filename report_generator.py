import general_report as gen_report
import order_report as ord_report
import product_report as prd_report

import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
import io_operations as io



def order_info_table(df, purchase_agreement):
    fig = go.Figure(data=[go.Table(header=dict(values=[purchase_agreement, 'Results']),
                 cells=dict(values=[
                     [purchase_agreement, "No. Companies dealt", "No. Areas dealt", "Products Sold", "New Products Sold", "Refurbished Products Sold"], 
                     [gen_report.count_orders(df), 
                     gen_report.count_companies(df), 
                     gen_report.count_counties(df), 
                     gen_report.count_products(df), 
                     gen_report.count_new_products(df), 
                     gen_report.count_refurbished_products(df)]]))
                     ])
    fig.update_layout(title_text = f"{purchase_agreement.capitalize()} Table", width=500, height= 400)
    return fig.to_html(full_html=True, include_plotlyjs='cdn') 
