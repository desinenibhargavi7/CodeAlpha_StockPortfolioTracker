# CodeAlpha Task 2: Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

stock_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in stocks:
    price = stocks[stock_name]
    total = price * quantity

    print("\n----- Stock Portfolio -----")
    print("Stock:", stock_name)
    print("Quantity:", quantity)
    print("Price per share: $", price)
    print("Total Investment: $", total)
else:
    print("Stock not found.")