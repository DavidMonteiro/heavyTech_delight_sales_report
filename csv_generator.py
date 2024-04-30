import random
from faker import Faker
import datetime
import pandas as pd

def generate_sales_data(num_rows=100):


    """ Define the possible options for nominal columns in lists"""
    finance_types = ['sale', 'rental']
    sellers = ['James Ford', 'Kate Austen', 'John Locke', 'Jack Shephard']
    business_sectors = ['Construction', 'Mining', 'Infrastructure', 'Demolition', 'Landscaping']
    product_makes = ['Caterpillar', 'Komatsu', 'Volvo', 'Haulage']
    product_types = ['Bulldozer', 'Excavator', 'Crane', 'Dump Truck', 'Backhoe Loader', 'Front End Loader', 'Concrete Pump Truck', 'Paver']
    product_states = ['new', 'refurbished']
    counties = ['Dublin', 'Cork', 'Galway', 'Limerick', 'Waterford', 'Kilkenny', 'Wexford', 'Meath', 'Kerry']

    # Create a Faker instance to generate fictional data
    fake = Faker()

    # Create a list to hold the data rows
    sales_data = []

    # Generate 100 rows of data
    for _ in range(num_rows=100):
        date = fake.date_between(start_date=datetime.date(2021, 1, 1), end_date=datetime.date(2021, 12, 30))
        finance_type = random.choice(finance_types)
        order_no = str(random.randint(10000, 99999))
        seller = random.choice(sellers)
        company = fake.company()
        county = random.choice(counties)
        business_sector = random.choice(business_sectors)
        product_state = random.choice(product_states)
        product_make = random.choice(product_makes)
        product_model = fake.lexify(text='??????')
        product_type = random.choice(product_types)
        product_quantity = random.randint(1, 4)
        
        sales_data.append([
            date, 
            finance_type, 
            order_no, 
            seller, 
            company, 
            county, 
            business_sector, 
            product_state, 
            product_make, 
            product_type, 
            product_model, 
            product_quantity
            ])


    # Create a DataFrame
    columns = [
        "Date",
        "Finance_Type",
        "Order_no",
        "Seller",
        "Company",
        "County",
        "Business_Sector",
        "Product_State",
        "Product_Make",
        "Product_Type",
        "Product_Model",
        "Product_Quantity"
        ]
    df = pd.DataFrame(sales_data, columns=columns)

    # Save the DataFrame to a CSV file
    df.to_csv('heavyTech_delight_sales_2021.csv', index=False)