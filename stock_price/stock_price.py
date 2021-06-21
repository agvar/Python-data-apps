import argparse
import datetime
import streamlit as st
import yfinance as yf
import pandas as pd

def stock_price(ticker1,ticker2,start_date,end_date,period):
    """
    :param ticker1: first ticker symbol for comparison
    :param ticker2: second ticket symbol for comparison
    :param start_date: start date for the ticker data
    :param end_date: end date for the ticker data
    :param period: period for the ticker data
    :return: None
    """
    st.write("# Stock Price Comparison App")
    tickerSymbol1= ticker1
    tickerData1=yf.Ticker(tickerSymbol1)
    tickerDF1=tickerData1.history(period=period,start=start_date,end=end_date)

    tickerSymbol2= ticker2
    tickerData2=yf.Ticker(tickerSymbol2)
    tickerDF2=tickerData2.history(period=period,start=start_date,end=end_date)

    key_list=[tickerSymbol1,tickerSymbol2]
    TickerDFVol= pd.concat([tickerDF1["Volume"],tickerDF2["Volume"]],axis=1,keys=key_list)
    st.write("## Stock Price Comparison by Volume")
    st.write(TickerDFVol)
    st.line_chart(TickerDFVol)

    TickerDFClose = pd.concat([tickerDF1["Close"], tickerDF2["Close"]], axis=1, keys=key_list)
    st.write("## Stock Price by Comparison by Closing Price")
    st.write(TickerDFClose)
    st.line_chart(TickerDFClose)


if __name__=="__main__":
    my_parser=argparse.ArgumentParser(description='Specify the stock symbol to be displayed')
    my_parser.add_argument('ticker1',metavar='ticker',type=str,help='Name of Ticker Symbol 1')
    my_parser.add_argument('ticker2', metavar='ticker', type=str, help='Name of Ticker Symbol 2')
    my_parser.add_argument('start_date', metavar='start_date', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'), help='Start date of Ticker')
    my_parser.add_argument('end_date', metavar='end_date', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'), help='End date of Ticker')
    my_parser.add_argument('period', metavar='period', type=str,help='Period of the Ticker-format')
    args=my_parser.parse_args()
    ticker1=args.ticker1
    ticker2 = args.ticker2
    start=args.start_date
    end=args.end_date
    period=args.period
    stock_price(ticker1,ticker2,start,end,period)