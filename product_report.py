import plotly.graph_objects as go


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





def product_Analysis(df, html_content0):
    """Master function to generate call functions above, stored them in a string and return them """

    html_content0 +=  "<h2 id=\"Product Information\">Product Information</h2>"

    # Generate the histogram chart
    product_treemap_fig = product_treemap(df)

    #Push chart into the html string
    html_content0 +=  product_treemap_fig

    return html_content0