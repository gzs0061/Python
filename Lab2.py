__author__ = 'Ella Seaman'
# Input List: weight_lbs
# Output List: weight_lbs, water_intake
#
# Declare Integer weight_lbs
# Declare Integer water_intake
#
# Display welcome message
# Display round to nearest whole number message
#
# Display "How much do you weigh? "
# Input weight_lbs
# Set water_intake = weight_lbs * 0.6
# Display "Your weight is", weight_lbs, "lbs."
# Display "You should be drinking", water_intake, "ounces of water daily."

weight_lbs = 0.00
water_intake = 0.00

print("Welcome to the water intake calculator! Enter your weight below in pounds(lbs).")
print("Please round to the nearest whole number (for example, 145.50 to 150lbs)")
print("then I will tell you how many ounces of water you should be drinking a day.")
print("")

weight_lbs = int(input("How much do you weigh? "))

water_intake = weight_lbs * 0.6

print("Your weight is", weight_lbs, "lbs.")
print("You should be drinking", water_intake, "ounces of water daily.")
