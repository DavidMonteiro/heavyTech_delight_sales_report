import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

def order_histogram(df): 
    """Function to create a histogram that compares sales every month between new products and refurbished products"""

    month_dict = {'January':1,'February':2,'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
    line_date_order = df.groupby(['Month', 'Quarter','Product_State'])['Order_no'].count().reset_index().sort_values('Month', key = lambda x : x.apply (lambda x : month_dict[x]))
    
    all_months = pd.DataFrame({'Month': list(month_dict.keys())})
    
    new_data = line_date_order[line_date_order['Product_State'] == 'new']
    refurbished_data = line_date_order[line_date_order['Product_State'] == 'refurbished']
    
    line_date_order =  line_date_order.groupby(["Month"]).sum().reset_index().set_index('Month').reindex(all_months['Month'], fill_value=0).reset_index()
    
    new_data = new_data.set_index('Month').reindex(all_months['Month'], fill_value=0).reset_index()
    refurbished_data = refurbished_data.set_index('Month').reindex(all_months['Month'], fill_value=0).reset_index()
    
    #Histogram 
    histogram = px.histogram(title=" Monthly Order Distribution: New vs. Refurbished", x=line_date_order['Month'], y=line_date_order['Order_no'], color_discrete_sequence =['#99d5b0'], 
                             text_auto=True, labels={'x':'Month', 'y':'Orders'}, category_orders={"Month": all_months})
    histogram.add_trace(
        go.Scatter(
            name='New',
            x= new_data['Month'],
            y= new_data.Order_no,
            marker=dict(color='purple')
        ))
    histogram.add_trace(
        go.Scatter(
            name='Refurbished',
            x= refurbished_data['Month'],
            y= refurbished_data.Order_no,
            marker=dict(color='orange')
        ))

    return histogram.to_html(full_html=True, include_plotlyjs='cdn')


def order_scatter(df):
    #Scatter Chart
    fig = px.scatter(df, x="Date", y="County", color="Business_Sector",
                 size='Product_Quantity', title="Distribution of Orders by County and Business", height=900)
    return fig.to_html(full_html=True, include_plotlyjs='cdn')

def order_county_diagram(df):
    #Subplot with horizontal bar chart and table for orders and the customer area
    county_order_count = df.groupby('County')['Order_no'].count()

    fig = make_subplots(
        rows=1, cols=2,
        shared_xaxes=True,
        vertical_spacing=0.03,
        specs=[[{"type": "table"},
               {"type": "bar"}]]
    )

    fig.add_trace(
        go.Table(
            header=dict(
                values=['Counties:', 'Orders Made:']
            ), 
            cells=dict(
                values=[county_order_count.sort_values(ascending=False).index, 
                         county_order_count.sort_values(ascending=False).values]
            )),
        row=1, col=1
    )

    fig.add_trace(
        go.Bar( 
            y=county_order_count.values, 
            x=county_order_count.index,
            marker=dict(
                color='rgba(50, 171, 96, 0.6)',
                line=dict(color='rgba(50, 171, 96, 1.0)')
            )),
        row=1, col=2
    )

    fig.update_layout(
        height=400,
        showlegend=False,
        title_text="Counties",
    )

    return fig.to_html(full_html=True, include_plotlyjs='cdn')

def order_Analysis(df, html_content0):
    """Master function to generate call functions above, stored them in a string and return them """

    html_content0 +=  "<h2 id=\"Order Information\">Order Information</h2>"

    # Generate the histogram chart
    histogram_fig = order_histogram(df)
    scatter_fig = order_scatter(df)
    counties_fig = order_county_diagram(df)

    #Push chart into the html string
    html_content0 +=  histogram_fig
    html_content0 += scatter_fig
    html_content0 += counties_fig

    return html_content0

