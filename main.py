import csv
import pandas as pd
import yfinance as yf

# Get the ticker list and iterate through; Price of stock should be greater than 10
# Download the percent_change data from (https://www.barchart.com/stocks/performance/five-day-gainers/advances?viewName=main&orderBy=percentChange5d&orderDir=desc)

df = pd.read_csv('percent_change.csv')
df = df[df['Last'] >= 10]
x = list(df.iloc[:-1,0])

for each in x:
    ticker_symbol = each
    z_score, curr_price = 0, 0

    # Create a Ticker object
    ticker = yf.Ticker(ticker_symbol)

    # Get the historical data and compute the z-score
    historical_data = ticker.history(period="20d")  # data for the last year

    try:
        curr_price = historical_data["Close"][19]
    except:
        pass

    # Get the mean and std for last 6 days; excluding current day
    try:
        mean = historical_data.iloc[:-1,3].mean()
        standard_dev = historical_data.iloc[:-1,3].std()
        # print(mean)
        # print(standard_dev)
        z_score = ((curr_price - mean)/standard_dev)
    except:
        pass

    if (abs(z_score) >= 4):
        print(ticker_symbol, "- Mean Revert")
    else:
        pass
        # print(ticker_symbol, "- Don't Mean Revert")






