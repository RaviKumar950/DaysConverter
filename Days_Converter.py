# Get user input for the number of days
total_days = int(input("Enter the number of days: "))

# Calculate years, months, and remaining days
years = total_days // 365
remaining_days_after_years = total_days % 365
months = remaining_days_after_years // 30
remaining_days = remaining_days_after_years % 30

# Print the results
print(f"{total_days} days is approximately equal to:{years} years,\n{months} months, and\n{remaining_days} days.")# \n uses for the next line 