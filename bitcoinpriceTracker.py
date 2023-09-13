import requests
import os
import threading
import time
import pandas as pd
import matplotlib.pyplot as plt
import pandas
from PIL import Image


def priceExtractor(crypto_name):
    api_url = f"https://api.coincap.io/v2/assets/{crypto_name}"
    response = requests.get(api_url)
    resp_value = response.json()
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    filecreator(resp_value, current_time)


def filecreator(resp, current_time):
    if (os.path.isfile("priceStorage.csv")):
        with open("priceStorage.csv", 'a+') as f:
            f.write(f"{current_time},{resp['data']['priceUsd']}\n")
    else:
        with open("priceStorage.csv", "w") as f:
            f.write("current_time,priceUsd\n")
            f.write(f"{current_time},{resp['data']['priceUsd']}\n")


if __name__ == "__main__":
    for n in range(100):
        priceExtractor('bitcoin')
        time.sleep(1)

    # Converting CSV to Excel
    data = pd.read_csv('priceStorage.csv')
    data.to_excel("priceExcel.xlsx", header=True, index=False)

    # Creating a plot for bitcoin prices

    df = pd.read_csv('priceStorage.csv')
    plt.plot(df['current_time'], df['priceUsd'])
    plt.title("Bitcoin Price Trends")
    plt.xticks(rotation=45)
    plt.xlabel("Price")
    plt.ylabel("Time")
    plt.savefig('my_chart.png', dpi=300, orientation='portrait')

    # Opening Image automatically
    im = Image.open('my_chart.png')
    im.show()
