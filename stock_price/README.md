# Stock Price Comparison using Streamlit


Stock Price Comparison is a utility that creates a comparison chart of Volume and Closing prices between two stocks.
Below is a sample chart comparison of GOOGL and MSFT
![alt text](https://github.com/agvar/Python-data-apps/stock_price/stock_price_displayjpg.jpg)

## Prerequisites

Before you begin, ensure you have met the following requirements:
* Version of python used - Python 3.7.4

## Installing Stock Price Comparison

To install the project, the following packages are needed:

1. pip install streamlit
2. pip install yfinance
3. pip install matplotlib

## Using Stock Price Comparison

To use stock proce comparison, follow these steps:

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

## Contributing to Stock Price Comparison
To contribute to <project_name>, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Credits
* [@scottydocs](https://github.com/scottydocs)
* https://www.youtube.com/watch?v=JwSS70SZdyM&t=352s&ab_channel=freeCodeCamp.org
* https://aroussi.com/post/python-yahoo-finance

## Contact

If you want to contact me you can reach me at geevia2020@gmail.com
