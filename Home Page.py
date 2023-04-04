import numpy as np # linear algebra
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
import calendar 
import numpy as np
from PIL import Image
st.set_page_config(page_title="Dods Market Basket", page_icon=":maoi:",layout="wide"    )





#############################################################


df = pd.read_csv("jetson-sample-data.csv")


########################################################
st.image("HomePage2.png")
st.header("Top 5 Chart")
col11,col22 = st.columns(2)
with col11:
    year = st.selectbox(
        'Select Year',
        (2021,2022,2023))

    df['date'] = pd.to_datetime(df['date'])
   

    

# Sort the DataFrame by the 'date' column in ascending order
with col22:
    df = df.sort_values('date')
    df['date'] = pd.to_datetime(df.date, format='%Y-%m-%d')
    mon = df[ (df['date'].dt.year == year)]

    # Group data by item_name and sum up the quantity sold
    item_sales = mon.groupby('item_name')['quantity'].sum()

    # Sort the item_sales Series in descending order and get the top 5 items
    top_items = item_sales.sort_values(ascending=False).head(5)
    c = ["#fd7f6f", "#7eb0d5", "#b2e061", "#bd7ebe", "#ffb55a", "#ffee65", "#beb9db", "#fdcce5", "#8bd3c7","#1984c5", "#22a7f0", "#63bff0", "#a7d5ed", "#e2e2e2", "#e1a692", "#de6e56", "#e14b31", "#c23728", "orange"]


    # Plot a bar chart of the top 5 items
    fig, ax = plt.subplots(figsize=(10, 6))  # Set the width to 10 inches
    ax.bar(top_items.index, top_items.values, color = c)
    ax.set_title(f'Top 5 Items Sold in {year}')
    ax.set_xlabel('Item Name')
    ax.set_ylabel('Quantity Sold')
    st.write(fig)
    chart_data = pd.DataFrame(
        top_items.index,top_items.values,
        columns=top_items)
############################################################


st.header("Graph")

df['date'] = pd.to_datetime(df['date'])
mont = st.selectbox(
        'Select Month',
        ('January', 'February', 'March','April','May',"June","July","August","September","October","November","December"))
def get_month_number(month_name):
        # Convert month name to lowercase and get the corresponding month number
        try:
            month_number = list(calendar.month_name).index(month_name.lower().capitalize())
        except ValueError:
            raise ValueError('Invalid month name')
        return month_number
col1, col2, col3 = st.columns(3)
with col1: 
    year=2021
# Sort the DataFrame by the 'date' column in ascending order
    df = df.sort_values('date')
    df['date'] = pd.to_datetime(df.date, format='%Y-%m-%d')
    mon = df[(df['date'].dt.month == get_month_number(mont)) & (df['date'].dt.year == year)]

    # Group data by item_name and sum up the quantity sold
    item_sales = mon.groupby('item_name')['quantity'].sum()

    # Sort the item_sales Series in descending order and get the top 5 items
    top_items = item_sales.sort_values(ascending=False).head(5)
    c = ["#fd7f6f", "#7eb0d5", "#b2e061", "#bd7ebe", "#ffb55a", "#ffee65", "#beb9db", "#fdcce5", "#8bd3c7","#1984c5", "#22a7f0", "#63bff0", "#a7d5ed", "#e2e2e2", "#e1a692", "#de6e56", "#e14b31", "#c23728", "orange"]

    # Plot a bar chart of the top 5 items
    fig, ax = plt.subplots(figsize=(10, 8))  # Set the width to 10 inches
    ax.bar(top_items.index, top_items.values, color = c)
    ax.set_title(f'Top 5 Items Sold in {mont} {year}')
    ax.set_xlabel('Item Name')
    ax.set_ylabel('Quantity Sold')
    st.write(fig)
with col2:
    year=2022
    df = df.sort_values('date')
    df['date'] = pd.to_datetime(df.date, format='%Y-%m-%d')
    mon = df[(df['date'].dt.month == get_month_number(mont)) & (df['date'].dt.year == year)]

    # Group data by item_name and sum up the quantity sold
    item_sales = mon.groupby('item_name')['quantity'].sum()

    # Sort the item_sales Series in descending order and get the top 5 items
    top_items = item_sales.sort_values(ascending=False).head(5)
    c = ["#fd7f6f", "#7eb0d5", "#b2e061", "#bd7ebe", "#ffb55a", "#ffee65", "#beb9db", "#fdcce5", "#8bd3c7","#1984c5", "#22a7f0", "#63bff0", "#a7d5ed", "#e2e2e2", "#e1a692", "#de6e56", "#e14b31", "#c23728", "orange"]

    # Plot a bar chart of the top 5 items
    fig, ax = plt.subplots(figsize=(10, 8))  # Set the width to 10 inches
    ax.bar(top_items.index, top_items.values, color = c)
    ax.set_title(f'Top 5 Items Sold in {mont} {year}')
    ax.set_xlabel('Item Name')
    ax.set_ylabel('Quantity Sold')
    st.write(fig)
with col3:
    year=2023
    df = df.sort_values('date')
    df['date'] = pd.to_datetime(df.date, format='%Y-%m-%d')
    mon = df[(df['date'].dt.month == get_month_number(mont)) & (df['date'].dt.year == year)]

    # Group data by item_name and sum up the quantity sold
    item_sales = mon.groupby('item_name')['quantity'].sum()

    # Sort the item_sales Series in descending order and get the top 5 items
    top_items = item_sales.sort_values(ascending=False).head(5)
    c = ["#fd7f6f", "#7eb0d5", "#b2e061", "#bd7ebe", "#ffb55a", "#ffee65", "#beb9db", "#fdcce5", "#8bd3c7","#1984c5", "#22a7f0", "#63bff0", "#a7d5ed", "#e2e2e2", "#e1a692", "#de6e56", "#e14b31", "#c23728", "orange"]


    # Plot a bar chart of the top 5 items
    fig, ax = plt.subplots(figsize=(10, 8))  # Set the width to 10 inches
    ax.bar(top_items.index, top_items.values, color = c)
    ax.set_title(f'Top 5 Items Sold in {mont} {year}')
    ax.set_xlabel('Item Name')
    ax.set_ylabel('Quantity Sold')
    st.write(fig)

#st.line_chart(chart_data)

#bg
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-size: auto;
             background: rgb(6,0,46);
             background: linear-gradient(90deg, rgba(6,0,46,1) 100%, rgba(109,201,221,1) 100%, rgba(191,226,235,1) 100%, rgba(72,159,177,1) 100%);
             
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
st.text("Made by DODS")




    





# # Convert date column to datetime data type
# df['date'] = pd.to_datetime(df['date'])

# # Sidebar for user input

# # Filter data for selected month and year
# df_filtered = df[(df['date'].dt.month == month) & (df['date'].dt.year == year)]

# # Group data by item_name and sum up the quantity sold
# item_sales = df_filtered.groupby('item_name')['quantity'].sum()

# # Sort the item_sales Series in descending order and get the top 5 items
# top_items = item_sales.sort_values(ascending=False).head(5)

# # Bar chart of top 5 items
# st.title(f"Top 5 Items Sold in {month}/{year}")
# chart_data = pd.DataFrame({'Item': top_items.index, 'Quantity': top_items.values})
# chart = alt.Chart(chart_data).mark_bar().encode( x=alt.X('Item', axis=alt.Axis(labelAngle=0)), y='Quantity')
# st.altair_chart(chart, use_container_width=True)