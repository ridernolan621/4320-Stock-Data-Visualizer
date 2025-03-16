import requests
import pygal
import lxml

import key

def main():
    print("Stock Data Visualizer\n----------------------------\n")

    symbol = input("Enter the stock symbol you are looking for: ")
    print("----------------------------")

    chart = input("Enter chart type: \n1. Line \n2. Bar\n")
    print("----------------------------")
    chart_type = validate_chart(chart)

    time_series = input("Enter time series: \n1. Intraday \n2. Daily \n3. Weekly \n4. Monthly\n")
    print("----------------------------")
    time = validate_time(time_series)

    get_symbol(symbol, time)
    render_chart(chart_type)

def validate_chart(chart):
    while chart not in ['1', '2']:
        print("Invalid selection. Please enter a valid chart type.")
        chart = input("Enter chart type: \n1. Line \n2. Bar\n")
    return int(chart)

def validate_time(time):
    while time not in ['1', '2', '3', '4']:
        print("Invalid selection. Please enter a valid time series.")
        time = input("Enter time series: \n1. Intraday \n2. Daily \n3. Weekly \n4. Monthly\n")
    return int(time)

def get_symbol(symbol, time):
    series = None
    if time == 1:
        series = "TIME_SERIES_INTRADAY"
    elif time == 2:
        series = "TIME_SERIES_DAILY"
    elif time == 3:
        series = "TIME_SERIES_WEEKLY"
    elif time == 4:
        series = "TIME_SERIES_MONTHLY"

    url = f'https://www.alphavantage.co/query?function={series}&symbol={symbol}&interval=5min&apikey={key.key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        return response.status_code

def render_chart(chart_type):
    if chart_type == 1:
        line_chart()
    elif chart_type == 2:
        bar_chart()

def line_chart():
    return 0

def bar_chart():
    return 0

if __name__ == "__main__":
    main()
