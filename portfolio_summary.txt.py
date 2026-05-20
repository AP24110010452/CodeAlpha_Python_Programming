# Save the portfolio result to a text file
with open("portfolio_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("=======================\n")
    file.write(f"Total Portfolio Value: ₹{total_value}\n")

print("Portfolio summary has been saved to portfolio_summary.txt")