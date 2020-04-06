import requests
from matplotlib import pyplot as plt
import pandas as pd

from page.liveblogs import Liveblogs

values = []
dates = []


while True:
    daterange = pd.date_range(start=input('Enter start date: '),
                              end=input('Enter end date: ')).tolist()

    keyword = input('Enter keyword: ')

    for single_date in daterange:
        month = (single_date.strftime("%B"))
        day = (single_date.strftime("%d").lstrip('0'))
        year = (single_date.strftime("%Y"))

        page_content = requests.get(f'https://www.timesofisrael.com/liveblog-{month}-{day}-{year}/').content
        page = Liveblogs(page_content)

        dates.append(single_date.strftime("%b %d %y"))

        count = 0

        for headline in page.blocks:
            if keyword in headline.headline:
                count += 1
                print(f'\n {month} {day}: ', headline.headline)
        values.append(count)

    plt.plot(dates, values)
    plt.title(f'"{keyword}"')
    plt.xlabel("Date")
    plt.ylabel("Mentions")
    plt.show()








