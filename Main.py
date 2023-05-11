import pandas as pd
df_sp500 = pd.read_excel("C:/Users/12345/Downloads/SP500.xlsx",sheet_name="TICKER")
#Making dictionary for each ticker in SP500
sp500= dict()
for ticker in range (0,500):
    sp500[df_sp500.iloc[ticker][0]]= dict()
#Storing values inside each ticker
for ticker in sp500:
    df_ticker = pd.read_excel("C:/Users/12345/Downloads/SP500.xlsx",sheet_name=ticker)
    for x in range(0,len(df_ticker.index)):
        #Convert timestamp to string
        timestamp=df_ticker.iloc[x][0]
        #Convert dataframe to string
        Date=timestamp.strftime('%Y-%m-%d')
        #Assign Values
        sp500[ticker][Date] = {
            0: df_ticker.iloc[x][1],  # Open
            1: df_ticker.iloc[x][2],  # High
            2: df_ticker.iloc[x][3],  # Low
            3: df_ticker.iloc[x][4],  # Close
            4: df_ticker.iloc[x][5]}   # Volume
