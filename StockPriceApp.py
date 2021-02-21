# Showing the Apple Stock Price (AAPL) in a web browser using Python and Streamlit. 

# Streamlit is a Python library which enables a development of Data Science apps and provides an interactive web app


#pip install streamlit
#pip install yfinance


import yfinance as yf
import streamlit as st
import pandas as pd


# App header
st.write("""
# Apple Stock Price
Shown are the stock **closing price** and ***volume***!
""")


# ticker symbol
ticker = 'AAPL'


# get data
data = yf.Ticker(ticker)


# get historical prices 
ticker_hist = data.history(period='1d', start='2010-1-31', end='2021-1-31')


st.write("""
## Closing Price
""")
st.line_chart(ticker_hist.Close)


st.write("""
## Volume 
""")
st.line_chart(ticker_hist.Volume)




# Open Command Prompt: 	     conda activate dp
#                            cd C:\Users\user\GitHub\apps                   
#                            streamlit run StockPriceApp.py       -> runs the app in your browser
