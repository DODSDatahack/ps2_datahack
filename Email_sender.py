import openai
import pandas as pd
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
import streamlit as st
sender_mail = "dods.sender@gmail.com"

app_pass = "YOUR_APP_PASSWORD"

SHEET_ID = "1jYolDLbd5B-RyWRjrkIcjIlh9NFQHC-4DUuhDJDrTFQ"
SHEET_NAME = "Returning_Customers_Data"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"
# Set up the OpenAI API
openai.api_key = "YOUR_API_KEY"

# Load the dataset
df = pd.read_csv('jetson-sample-data.csv')

# Convert the date column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Calculate the maximum date for each client
max_dates = df.groupby('client_id')['date'].max().reset_index()

# Calculate the number of days since the maximum date for each client
max_dates['days_since_last_purchase'] = (datetime.today() - max_dates['date']).dt.days

# Identify the customers who have not returned for more than 30 days
inactive_customers = max_dates[max_dates['days_since_last_purchase'] > 30]['client_id']
inactive_customers = inactive_customers.drop_duplicates()
inactive_customers = pd.read_csv(URL)
num =0
st.title("Customer Acquisition Email Campaigns")    
# Generate personalized messages using ChatGPT and send feedback emails to inactive customers
mode = st.selectbox('Select mode: ', ("Send to inactive Customers", "Send a customized email"))
st.write("")
st.write("")
st.write("")
st.write("")

if mode == "Send to inactive Customers":
    if st.button("Send to all"):
        msg_ = "Sending..."
        st.write(msg_)
        while num < len(inactive_customers):
                # Generate a personalized message using ChatGPT

                prompt = f"Generate a personalized message by DODS for customer {inactive_customers.at[num, 'Name']} to encourage them to return to our store."
                response = openai.Completion.create(
                    engine="text-davinci-002",
                    prompt=prompt,
                    temperature=0.7,
                    max_tokens=100,
                    n=1,
                    stop=None,
                    timeout=10
                )
                message = response.choices[0].text.strip()
                receiver_mail =  inactive_customers.at[num, 'Email']
                
                
                
                #Check if the message is less than 50 words
                if len(message.split()) <= 50:
                    # Customize the email body with the generated message
                    email_body = f"{message}"

                    # Create the email message
                    msg = MIMEText(email_body)
                    msg['Subject'] = "Come back and get a 10% Discount!"
                    msg['From'] = sender_mail
                    msg['To'] = receiver_mail

                    # Send the email
                    s = smtplib.SMTP('smtp.gmail.com', 587)
                    s.starttls()
                    s.login(sender_mail, app_pass)
                    s.sendmail(sender_mail, receiver_mail, msg.as_string())
                    s.quit()
                num+=1
        msg_= "Sent!"
conf =  False
if mode == "Send a customized email":
     
     receiver_mail = st.text_input("Enter the Email ID of the receiver: ")
     email_body = st.text_input("Enter the body")

     
     msg = MIMEText(email_body)
     msg['Subject'] = st.text_input("Subject")
     msg['From'] = sender_mail
     msg['To'] = receiver_mail
     conf = st.button("Send") 
     if conf:

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_mail, app_pass)
        s.sendmail(sender_mail, receiver_mail, msg.as_string())
        s.quit()
        st.write("Sent!")
