import plotly.graph_objects as go
from plotly.subplots import make_subplots


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


def product_Analysis(df, html_content0):
    """Master function to generate call functions above, stored them in a string and return them """

    html_content0 +=  "<h2 id=\"Product Information\">Product Information</h2>"

    # Generate the histogram chart
    product_treemap_fig = product_treemap(df)
    top_pieChart_fig = product_pie_chart(df)

    #Push chart into the html string
    html_content0 +=  product_treemap_fig
    html_content0 += top_pieChart_fig

    return html_content0