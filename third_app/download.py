import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly' +
    '/datasets/master/2011_february_us_airport_traffic.csv')

df.to_csv("airport_traffic.csv")
