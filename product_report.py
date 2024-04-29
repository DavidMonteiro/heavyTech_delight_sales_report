import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px


def product_treemap(df):
    product_type_counts = df['Product_Make'].value_counts()

    # Create a treemap trace
    fig = go.Figure(go.Treemap(
        labels=product_type_counts.index,
        parents=['Makes'] * len(product_type_counts),  # Set parent as 'Products' for all labels
        values=product_type_counts.values
    ))

    # Update layout
    fig.update_layout(title='Treemap of Products sold by Make')

    # return the plot in html syntax
    return fig.to_html(full_html=True, include_plotlyjs='cdn')  


def product_pie_chart(df):
    # Top Products by Brand Pie Charts

    grouped_data = df.groupby(['Product_Make', 'Product_Type'])['Product_Quantity'].sum().reset_index()
    sum_product_quantity = grouped_data.groupby('Product_Make')['Product_Quantity'].sum()
    
    ordered_df = grouped_data.merge(sum_product_quantity, left_on='Product_Make', right_index=True)
    ordered_df = ordered_df.sort_values(by='Product_Quantity_y', ascending=False).drop('Product_Quantity_y', axis=1)

    #Check the number of unique product makes to ensure I select the right function to call   
    if len(ordered_df['Product_Make'].unique()) > 3:
        return top_four_pie_product(ordered_df)
    elif len(ordered_df['Product_Make'].unique()) > 1:
        return top_two_pie_product(ordered_df)
    elif len(ordered_df['Product_Make'].unique()) > 0:
        return top_one_pie_product(ordered_df)
    else:
         return "<span>Not enough products sold to generate diagrams</span>"  

def top_four_pie_product(ordered_df):
    best_product_1 = ordered_df[ordered_df['Product_Make'] == ordered_df['Product_Make'].unique()[0]]
    best_product_2 = ordered_df[ordered_df['Product_Make'] == ordered_df['Product_Make'].unique()[1]]
    best_product_3 = ordered_df[ordered_df['Product_Make'] == ordered_df['Product_Make'].unique()[2]]
    best_product_4 = ordered_df[ordered_df['Product_Make'] == ordered_df['Product_Make'].unique()[3]]

    # Create subplots with 2 rows and 2 columns
    fig = make_subplots(rows=2, cols=2, subplot_titles=[
        ordered_df['Product_Make'].unique()[0], 
        ordered_df['Product_Make'].unique()[1], 
        ordered_df['Product_Make'].unique()[2], 
        ordered_df['Product_Make'].unique()[3]], 
                        specs=[[ {"type": "pie"}, {"type": "pie"}],[ {"type": "pie"}, {"type": "pie"}]
                              ])



    # Add pie charts to the subplots
    fig.add_trace(go.Pie(labels=best_product_1['Product_Type'], values=best_product_1['Product_Quantity_x'], name=ordered_df['Product_Make'].unique()[0]), row=1, col=1)
    fig.add_trace(go.Pie(labels=best_product_2['Product_Type'], values=best_product_2['Product_Quantity_x'], name=ordered_df['Product_Make'].unique()[1]), row=1, col=2)
    fig.add_trace(go.Pie(labels=best_product_3['Product_Type'], values=best_product_3['Product_Quantity_x'], name=ordered_df['Product_Make'].unique()[2]), row=2, col=1)
    fig.add_trace(go.Pie(labels=best_product_4['Product_Type'], values=best_product_4['Product_Quantity_x'], name=ordered_df['Product_Make'].unique()[3]), row=2, col=2)
    
    
    
    fig.update_layout(height=700,showlegend=True)

    # Update layout and title
    fig.update_layout(title_text='Top Products by Brand Pie Charts', showlegend=True, annotations=[dict(text=ordered_df['Product_Make'].unique()[0], font_size=16, showarrow=False),
                     dict(text=ordered_df['Product_Make'].unique()[1], showarrow=False, font_size=16),
                     dict(text=ordered_df['Product_Make'].unique()[2], showarrow=False, font_size=16),
                     dict(text=ordered_df['Product_Make'].unique()[3], showarrow=False, font_size=16)])

    # return top 4 charts
    return fig.to_html(full_html=True, include_plotlyjs='cdn')
    

def top_two_pie_product(ordered_df):
    best_product_1 = ordered_df[ordered_df['Product_Make'] == ordered_df['Product_Make'].unique()[0]]
    best_product_2 = ordered_df[ordered_df['Product_Make'] == ordered_df['Product_Make'].unique()[1]]

    # Create subplots with 2 rows and 2 columns
    fig = make_subplots(rows=1, cols=2, subplot_titles=[
        ordered_df['Product_Make'].unique()[0], 
        ordered_df['Product_Make'].unique()[1]],  
        specs=[[ {"type": "pie"}, {"type": "pie"}]])



    # Add pie charts to the subplots
    fig.add_trace(go.Pie(labels=best_product_1['Product_Type'], values=best_product_1['Product_Quantity_x'], name=ordered_df['Product_Make'].unique()[0]), row=1, col=1)
    fig.add_trace(go.Pie(labels=best_product_2['Product_Type'], values=best_product_2['Product_Quantity_x'], name=ordered_df['Product_Make'].unique()[1]), row=1, col=2)

    fig.update_layout(height=600)

    # Update layout and title
    fig.update_layout(title_text='Top Products by Brand Pie Charts', showlegend=True, 
                     annotations=[dict(text=ordered_df['Product_Make'].unique()[0], font_size=16, showarrow=False),
                     dict(text=ordered_df['Product_Make'].unique()[1], showarrow=False, font_size=16)])

    # return top 3 products
    return fig.to_html(full_html=True, include_plotlyjs='cdn')


def top_one_pie_product(ordered_df):
    best_product = ordered_df[ordered_df['Product_Make'] == ordered_df['Product_Make'].unique()[0]]

    # Create subplots with 2 rows and 2 columns
    fig = make_subplots(rows=1, cols=1, subplot_titles=[
        ordered_df['Product_Make'].unique()[0]],  
        specs=[[ {"type": "pie"}]])



    # Add pie charts to the subplots
    fig.add_trace(go.Pie(labels=best_product['Product_Type'], values=best_product['Product_Quantity_x'], name=ordered_df['Product_Make'].unique()[0]), row=1, col=1)

    fig.update_layout(height=500,showlegend=True)

    # Update layout and title
    fig.update_layout(title_text='Top Products by Brand Pie Charts', showlegend=True, 
                     annotations=[dict(text=ordered_df['Product_Make'].unique()[0], font_size=16, showarrow=False)])

    # return top product sold
    return fig.to_html(full_html=True, include_plotlyjs='cdn')

def product_bar_chart(df):
    # Bar Chart to compare product by state, type and quantity sold
    cap_prod_type = df.groupby(['Product_State', 'Product_Type'])['Product_Quantity'].sum().reset_index()

    end_result = ""
    
    fig = px.bar(cap_prod_type, x="Product_Type", y="Product_Quantity", color= "Product_State", labels=" ",
                 color_discrete_map={ # replaces default color mapping by value
                    "New": "#B19CD7", "Refurbished": "#99d5b0"
                },title='Products sold by Product type', width=950, height=500) 
    fig.update_traces(textfont_size=12, textangle=1, textposition="outside", cliponaxis=False)
    end_result += fig.to_html(full_html=True, include_plotlyjs='cdn')

    cap_prod_type = df.groupby(['Product_Type'])['Product_Quantity'].sum().reset_index()
    fig = go.Figure(data=[go.Table(header=dict(values=['Product Type', 'Total Sold']),
                     cells=dict(values=[
                         cap_prod_type.sort_values('Product_Quantity', ascending=False).head(n=5).Product_Type, 
                         cap_prod_type.sort_values('Product_Quantity', ascending=False).head(n=5).Product_Quantity]))
                         ])
    fig.update_layout(width=800, height=400)
    end_result += fig.to_html(full_html=True, include_plotlyjs='cdn')
    return end_result


def product_scatter(df):
    ##Scatter chart of products sold by make over the year and their condition

    scatter_sale_order = df[['Date', 'Product_Type', 'Product_Make']]

    fig = px.scatter(scatter_sale_order, x='Date', y='Product_Make', color='Product_Type',
                      title='Product Type vs. Product Quantity', height=500)

    return fig.to_html(full_html=True, include_plotlyjs='cdn')



def product_information(df):
    ##Subplot to show makes product type and poduct state by quarter

    # Group data by quarter and finance type for the stacked bar chart
    grouped_df = df.groupby(['Quarter', 'Product_State'])['Product_Quantity'].sum().reset_index()

    # Create subplots with 4 rows and 2 columns
    fig = make_subplots(rows=4, cols=3, subplot_titles=["Q1 Makes", "Q1 Product Types", "Q1 Product Condition",
             "Q2 Makes", "Q2 Product Types", "Q2 Product Condition", "Q3 Makes", "Q3 Product Types", "Q3 Product Condition",
             "Q4 Makes", "Q4 Product Types", "Q4 Product Condition"],
             specs=[[{"type": "treemap"}, {"type": "pie"}, {"type": "bar"}],
                    [{"type": "treemap"}, {"type": "pie"}, {"type": "bar"}],
                    [{"type": "treemap"}, {"type": "pie"}, {"type": "bar"}],
                    [{"type": "treemap"}, {"type": "pie"}, {"type": "bar"}]])

    # Loop through each quarter and create the pie and bar charts
    for quarter in range(1, 5):
        
        # Stacked bar chart data for the quarter
        bar_data = grouped_df[grouped_df['Quarter'] == quarter]    
        
        # Pie chart data for the quarter
        pie_data = df[df['Quarter'] == quarter]['Product_Type'].value_counts()

        #treemap data for the quarter
        product_type_counts = df[df['Quarter'] == quarter]['Product_Make'].value_counts()

        # Create tree chart
        tree_chart = go.Treemap(labels=product_type_counts.index, parents=['Makes'] * len(product_type_counts), values=product_type_counts.values)
        fig.add_trace(tree_chart, row=quarter, col=1)

        # Create pie chart
        pie_chart = go.Pie(labels=pie_data.index, values=pie_data.values, name=f"Q{quarter}")
        fig.add_trace(pie_chart, row=quarter, col=2)

        # Create stacked bar chart
        bar_chart = go.Bar(x=bar_data['Product_State'], y=bar_data['Product_Quantity'],
                           text=bar_data['Product_Quantity'], textposition='auto', name=f"Q{quarter}")
        fig.add_trace(bar_chart, row=quarter, col=3)

    # Update layout and title
    fig.update_layout(title_text="Product Information by Quarter",
                      showlegend=True,
                      height=1000,
                      width=1300)

    # return the plot in html syntax
    return fig.to_html(full_html=True, include_plotlyjs='cdn') 

def product_Analysis(df, html_content0):
    """Master function to generate call functions above, stored them in a string and return them """

    html_content0 +=  "<h2 id=\"Product Information\">Product Information</h2>"

    # Generate the histogram chart
    product_treemap_fig = product_treemap(df)
    top_pieChart_fig = product_pie_chart(df)
    bar_chart = product_bar_chart(df)
    scatter_fig = product_scatter(df)
    product_info_fig = product_information(df)

    #Push chart into the html string
    html_content0 +=  product_treemap_fig
    html_content0 += top_pieChart_fig
    html_content0 += bar_chart
    html_content0 += scatter_fig
    html_content0 += product_info_fig

    return html_content0