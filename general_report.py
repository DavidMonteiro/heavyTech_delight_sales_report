# Python script dedicated to General functions for sales report

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px



def count_orders(df): 
    """function to count orders"""
    return df['Order_no'].count()


def count_rentals(df):  
    """funcion to count hires"""
    return (df['Finance_Type'] == 'rental').sum()


def count_sales(df):  
    """function to count capital purchase"""
    return (df['Finance_Type'] == 'sale').sum()


def count_products(df): 
    """function to count products""" 
    return df['Product_Quantity'].sum()


def count_new_products(df): 
    """function to count New Products""" 
    return (df.loc[df['Product_State'] == 'new']).Product_Quantity.sum()


def count_refurbished_products(df):
    """Function to count S/Hand Products"""  
    return (df.loc[df['Product_State'] == 'refurbished']).Product_Quantity.sum()


def count_companies(df):  
    """Function to count no of unique companies"""
    return df['Company'].nunique()


def count_counties(df): 
    """Function to count no of unique counties"""
    return df['County'].nunique()




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


def general_bubble_chart(df):
    fig = px.scatter(df, x="Date", y="Business_Sector", color="Finance_Type",
                     size='Product_Quantity', title="Scatter Chart: Sales vs. Rentals", height=800)
    return fig.to_html(full_html=True, include_plotlyjs='cdn')