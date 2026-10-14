member_name = input("Enter member name: ")
age = int(input("Enter age: "))
price_per_session = float(input("Enter price per session: "))
sessions = int(input("Enter number of sessions: "))
calories_per_session = float(input("Enter calories burned per session: "))

full_amount = price_per_session * sessions
total_calories = calories_per_session * sessions
average_calories = total_calories / sessions

membership_discount = 200
membership_discount += 0

discount_amount = membership_discount
final_amount = full_amount - discount_amount

is_adult = age >= 18
is_expensive = full_amount > 2000
good_calorie_performance = average_calories > 300

print("\n===== FITNESS SUMMARY =====")
print(f"Member Name: {member_name}")
print(f"Age: {age}")
print(f"Price per Session: ₹{price_per_session:.2f}")
print(f"Number of Sessions: {sessions}")
print(f"Full Amount: ₹{full_amount:.2f}")
print(f"Discount Amount: ₹{discount_amount:.2f}")
print(f"Final Amount: ₹{final_amount:.2f}")
print(f"Total Calories Burned: {total_calories:.2f}")
print(f"Average Calories per Session: {average_calories:.2f}")
print(f"18 or Above: {is_adult}")
print(f"Total Cost Greater Than ₹2000: {is_expensive}")
print(f"Average Calories Greater Than 300: {good_calorie_performance}")

