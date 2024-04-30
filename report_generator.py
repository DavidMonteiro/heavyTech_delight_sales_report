import general_report as gen_report
import order_report as ord_report
import product_report as prd_report
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
import io_operations as io


def order_info_table(df, purchase_agreement):
    fig = go.Figure(
        data=[
            go.Table(
                header=dict(values=[purchase_agreement, 'Results']),
                cells=dict(values=[
                    [
                        purchase_agreement,
                        "No. Companies dealt",
                        "No. Areas dealt",
                        "Products Sold",
                        "New Products Sold",
                        "Refurbished Products Sold"
                    ],
                    [
                        gen_report.count_orders(df),
                        gen_report.count_companies(df),
                        gen_report.count_counties(df),
                        gen_report.count_products(df),
                        gen_report.count_new_products(df),
                        gen_report.count_refurbished_products(df)]
                ])
            )
        ])
    fig.update_layout(
        title_text=f"{purchase_agreement.capitalize()} Table",
        width=500, height=400
    )

    return fig.to_html(full_html=True, include_plotlyjs='cdn')


def rental_Analysis(df):
    rental_df = df[df['Finance_Type'] == 'rental']

    html_content = "<h2 id=\"Rental Analysis\">Rental Analysis</h2>"
    html_content += order_info_table(rental_df, "Rental")

    html_content += "<h3 id=\"Rental Order Information\">\
        Rental Order Information</h3>"
    html_content += ord_report.order_Analysis(rental_df)

    html_content += "<h3 id=\"Rental Product Information\">\
        Rental Product Information</h3>"
    html_content += prd_report.product_Analysis(rental_df)

    return html_content


def sale_Analysis(df):
    sale_df = df[df['Finance_Type'] == 'sale']

    html_content = "<h2 id=\"Sale Analysis\">Sale Analysis</h2>"
    html_content += order_info_table(sale_df, "Sale")

    html_content += "<h3 id=\"Sales Order Information\">\
        Sales Order Information</h3>"
    html_content += ord_report.order_Analysis(sale_df)

    html_content += "<h3 id=\"Sales Product Information\">\
        Sales Product Information</h3>"
    html_content += prd_report.product_Analysis(sale_df)

    return html_content


def completeAnalysis(df):

    general_index = """<h1>Complete Analysis</h1>
        <h2>Index</h2>
            <div>
                <ul>
                    <li><span><a href="#General-Information">\
                        General Analysis</a></span></li>
                    <li><span><a href="#Capital-Purchase-Analysis">\
                        Capital Purchase Analysis</a></span></li>
                        <ul>
                            <li><span>\
                            <a href="#Capital-Purchase-Order-Information">\
                            Orders Information</a></span></li>
                            <li><span>\
                            <a href="#Capital-Purchase-Product-Information">\
                            Product Information</a></span></li>
                        </ul>
                    <li><span><a href="#Hire-Analysis">\
                    Hire Analysis</a></span></li>
                        <ul>
                            <li><span><a href="#Hire-Order-Information">\
                            Orders Information</a></span></li>
                            <li><span><a href="#Hire-Product-Information">\
                            Product Information</a></span></li>
                        </ul>
                </ul>
            </div>"""

    html_content = general_index

    html_content += gen_report.general_Analysis(df)
    html_content += sale_Analysis(df)
    html_content += rental_Analysis(df)

    return html_content
