import openai
import pandas as pd
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText

# Set up the OpenAI API
openai.api_key = "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"

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

# Generate personalized messages using ChatGPT and send feedback emails to inactive customers
for customer in inactive_customers:
        # Generate a personalized message using ChatGPT
        prompt = f"Generate a personalized message for customer {customer} to encourage them to return to our store."
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

        # Check if the message is less than 50 words
        if len(message.split()) <= 50:
            # Customize the email body with the generated message
            email_body = f"{message} Come back and get a 10% discount on your next purchase."

            # Create the email message
            msg = MIMEText(email_body)
            msg['Subject'] = "Come back and get a 10% discount!"
            msg['From'] = "swarvjagdale.study@gmail.com"
            msg['To'] = "swarvjagdale.study@gmail.com"

            # Send the email
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("swarvjagdale.study@gmail.com", "subvulgivrvedasv")
            s.sendmail("swarvjagdale.study@gmail.com", "swarvjagdale.study@gmail.com", msg.as_string())
            s.quit()