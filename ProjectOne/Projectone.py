from datetime import datetime
import numpy as np

def extract_data("Nat_Gas.csv"):
    dates = []
    prices = []

    with open("Nat_Gas.csv", "r") as file:
        next(file)  # skip header

        for line in file:
            date_str, price_str = line.strip().split(",")

            # convert date (IMPORTANT FORMAT CHANGE)
            date = datetime.strptime(date_str, "%m/%d/%y")

            price = float(price_str)  

            dates.append(date)
            prices.append(price)

    return dates, prices


    def convert_to_days(dates):
        base = dates[0]
        days = [(d - base).days for d in dates]
    return days, base


   

def fit_model(days, prices):
    coeffs = np.polyfit(days, prices, 1)  # linear trend
    return coeffs
