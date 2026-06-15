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


def price_storage_contract(
        injection_dates,
        withdrawal_dates,
        volumes,
        get_price,
        max_capacity,
        inject_rate,
        withdraw_rate,
        storage_cost_per_day):

    total_profit = 0
    inventory = 0

    for inj_date, wd_date, volume in zip(
            injection_dates,
            withdrawal_dates,
            volumes):

        volume = min(volume, inject_rate)
        volume = min(volume, withdraw_rate)

        if inventory + volume > max_capacity:
            raise ValueError("Storage capacity exceeded")

        buy_price = get_price(inj_date)
        sell_price = get_price(wd_date)

        days = (wd_date - inj_date).days

        storage_cost = (
            volume *
            storage_cost_per_day *
            days
        )

        profit = (
            volume * sell_price
            - volume * buy_price
            - storage_cost
        )

        total_profit += profit

    return total_profit
