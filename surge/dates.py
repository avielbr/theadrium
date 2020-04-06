import pandas as pd


daterange = pd.date_range(start = input('Enter start date: '), end = input('Enter end date: ')).tolist()

for single_date in daterange:
    month = (single_date.strftime("%B"))
    day = (single_date.strftime("%-d"))
    print (f'{month} {day}')