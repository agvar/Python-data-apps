# Stock Price Comparison using Streamlit


Stock Price Comparison is a utility that creates a comparison chart of Volume and Closing prices between two stocks. The app uses the yfinance library to get historical stock price data and the Streamlit library to create a web app that displays the comparison charts.

Below is a sample chart comparison of GOOGL and MSFT

![alt text](https://github.com/agvar/Python-data-apps/blob/9cbb0804094a7cb5cd10127d6748c6fdf529b388/stock_price/stock_price_displayjpg.jpg)

## Prerequisites

Before you begin, ensure you have met the following requirements:
* Version of python used - Python 3.7.4

## Installing Stock Price Comparison

To install the project, the following packages are needed:

1. pip install streamlit
2. pip install yfinance
3. pip install pandas

## Using Stock Price Comparison

To use stock price comparison, follow these steps:

```
streamlit run stock_price.py <stock1> <stock2> <start date> <end date> <period>
```
#### Permissible values for the command line arguments :
1. stock1 : Ticker symbol of the first stock
2. stock2 : Ticker symbol of the second stock
3. start date : Start date string (YYYY-MM-DD) or datetime
4. end date : End date string (YYYY-MM-DD) or datetime
5. period : data period used .Valid periods are: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max

#### example for Google and Apple stock comparison from 2015-01-01 to 2021-06-01 for a day period
```
streamlit run stock_price.py GOOGL MSFT 2015-01-01 2021-06-01 1d
```
