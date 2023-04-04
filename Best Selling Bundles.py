# import libraries
import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
import matplotlib.pyplot as plt
import streamlit as st
st.set_page_config(page_title="Dods Market Basket", page_icon=":maoi:",layout="wide")

# load data
df = pd.read_csv('jetson-sample-data.csv')
st.header(f"Top selling bundles")

options2 = np.arange(start=3, stop=21, step=2)
numb = st.selectbox("Enter the number of bundles required", options2)

# convert item names to a list of lists


item_lists = df.groupby('order_id')['item_name'].apply(list).values.tolist()

# use TransactionEncoder to one-hot encode the item lists
te = TransactionEncoder()
te_ary = te.fit_transform(item_lists)

# convert the one-hot encoded data to a pandas DataFrame
df_onehot = pd.DataFrame(te_ary, columns=te.columns_)

# find frequent itemsets with at least two items
frequent_itemsets = apriori(df_onehot, min_support=0.01, use_colnames=True, max_len=2)

# filter to keep only itemsets with two or more items
bundles = frequent_itemsets[frequent_itemsets['itemsets'].apply(lambda x: len(x) >= 2)]

# sort by support and keep only the top 10 bundles
top_bundles = bundles.sort_values(by='support', ascending=False).head(numb)

# plot a bar chart of the top 10 bundles
fig, ax = plt.subplots(figsize=(8, 6))  # Set the width to 10 inches


ax.barh(range(len(top_bundles)), top_bundles['support'],color = ["#fd7f6f", "#7eb0d5", "#b2e061", "#bd7ebe", "#ffb55a", "#ffee65", "#beb9db", "#fdcce5", "#8bd3c7","#1984c5", "#22a7f0", "#63bff0", "#a7d5ed", "#e2e2e2", "#e1a692", "#de6e56", "#e14b31", "#c23728", "orange"])
plt.yticks(range(len(top_bundles)), [' & '.join(list(x)) for x in top_bundles['itemsets']])
plt.xlabel('Support')
plt.ylabel('Bundle')
plt.title(f'Top {numb} Best Selling Bundles')

st.write(fig)
def add_bg_from_url():
 st.markdown(
        f"""
        <style>
        .stApp {{
            background: rgb(6,0,46);
            background: linear-gradient(90deg, rgba(6,0,46,1) 100%, rgba(109,201,221,1) 100%, rgba(191,226,235,1) 100%, rgba(72,159,177,1) 100%);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_url()
st.text("Made by DODS")