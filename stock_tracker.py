prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330
}

total_value = 0

print("=== Simple Stock Portfolio Tracker ===")
print("Available stocks:", ", ".join(prices.keys()))

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in prices:
        print("Stock not available.")
        continue

    quantity = int(input(f"Enter quantity for {stock}: "))
    investment = prices[stock] * quantity
    total_value += investment

    print(f"{stock}: ₹{prices[stock]} x {quantity} = ₹{investment}")

print("\nTotal Portfolio Value: ₹", total_value)

with open("portfolio_summary.txt", "w") as file:
    file.write(f"Total Portfolio Value: ₹{total_value}")

print("Summary saved to portfolio_summary.txt")