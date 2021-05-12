income = float(0)
tax = float(0)

print("Please enter your income:")
income = float(input())

if income <= 10000:
  tax = 0.02 * income
if income > 10000:
  tax = 0.08 * (income - 10000) + 200

print("Tax amount: $" + str(tax))


income = int(input())
print("My income is $" + str(income))

