share_price = 150
shares = 10 # 10 shares of Apple stock
years = 3 # assuming this

new_share_price = 175

initial_investment = share_price * shares
current_investment_value = new_share_price * shares

profit = current_investment_value - initial_investment

return_pct = (profit/initial_investment) * 100
annualized_return = ((current_investment_value/initial_investment) ** (1/years) -1) * 100

print("INVESTMENT CALCULATOR")

print(f"Initial Investment: ${initial_investment}")

print(f"Final Value: ${current_investment_value}")

print(f"Profit: ${profit}")

print(f"Investment Return: ${return_pct:.2f}%")
print(f"Annualized Return: {annualized_return:.2f}%")