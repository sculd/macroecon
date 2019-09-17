import pandas as pd

df_bonds = pd.read_csv('data_no_nd.csv', parse_dates=['time'], infer_datetime_format=True)
df_bonds = df_bonds[df_bonds.time.dt.day==1].drop(['m01', 'm03', 'm06', 'y02', 'y03', 'y05', 'y07'], axis=1).set_index('time').astype('float32') * 100

df_gold = pd.read_csv('gold-prices/monthly_csv.csv', parse_dates=['date'], infer_datetime_format=True)
df_gold = df_gold.set_index('date')

df = pd.concat([df_bonds, df_gold], axis=1)


df_employment = pd.read_csv('employment-us/data/aat1_csv.csv', parse_dates=['year'], infer_datetime_format=True)
df_employment = df_employment.set_index('year')[['unemployed_percent']]


pd.concat([df, df_employment], axis=1)
pd.concat([df, df_employment])


df_housing = pd.read_csv('house-prices-us/data/cities_csv.csv', parse_dates=['Date'], infer_datetime_format=True)
df_housing = df_housing.set_index('Date')[['National-US']]

df = pd.concat([df, df_housing], axis=1)

df_sp500 = pd.read_csv('stock-index/sp500.csv', parse_dates=['Date'], infer_datetime_format=True)
df_sp500 = df_sp500[df_sp500.Date.dt.day==1].set_index('Date')[['AdjClose', 'Volume']]
df_sp500 = df_sp500.rename(columns={'AdjClose': 'sp500_price', 'Volume': 'sp500_volume'})

df = pd.concat([df, df_sp500], axis=1)

df_fed_rate = pd.read_csv('fed-target-interest-rate/FEDFUNDS.csv', parse_dates=['Date'], infer_datetime_format=True)
df_fed_rate = df_fed_rate[df_fed_rate.Date.dt.day==1].set_index('Date')
df_fed_rate = (df_fed_rate.rename(columns={'FEDFUNDS': 'fed_rate'}) / 0.25).round() * 0.25 * 100

df = pd.concat([df, df_fed_rate], axis=1)
df = df.interpolate()

df.to_csv('processed.csv')


cols = ['m03', 'y10', 'gold_price', 'sp500_price', 'sp500_volume', 'fed_rate']

