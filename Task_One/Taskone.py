# Task One

# Opens Nat_Gas as file and prints the contents
with open("Nat_Gas.csv", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# asks user to input date
input("Enter the month and year (mm/YYYY)")