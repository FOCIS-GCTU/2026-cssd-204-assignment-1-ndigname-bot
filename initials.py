# File: easter_date.py
# Description: This program calculates the date of Easter Sunday for any year given
#               using the Computus algorithm developed by Carl Friedrich Gauss.
# Assignment Number: 2
#
# Name: Emmanuel Ndignam Nelimo
# SID: 2425401719
# Email: 2425401719@live.gctu.edu.gh
# Grader: MR. AUGUSTUS BUCKMAN
# Slip days used this assignment: 0
#
# On my honor, Emmanuel Ndignam Nelimo, this programming assignment is my own work
# and I have not provided this code to any other student.

#  Ask the user for the year and save it in a variable named year
year = int(input("Enter year: "))

# Divide year by 19 and call the remainder lunar_year_cycle_position
# This will finds where the year falls in the 19-year Metonic cycle
lunar_year_cycle_position = year % 19

# Step 3: Divide year by 4 and call the remainder weekday_slide_part_1
# This helps adjust for leap year effects on weekdays
weekday_slide_part_1 = year % 4

# Step 4: Divide year by 7 and call the remainder weekday_slide_part_2
# This helps track the day of the week shift
weekday_slide_part_2 = year % 7

# Step 5: Divide year by 100 and call the quotient leap_year_100
# This finds the century (e.g., 2001 // 100 = 20)
leap_year_100 = year // 100

# Step 6: Divide leap_year_100 by 4 and call the quotient leap_year_400
# This finds how many 4-century blocks have passed
leap_year_400 = leap_year_100 // 4

# Step 7: Set lunar_orbit_correction to (13 + 8 x leap_year_100) divided by 25
# This corrects for inaccuracies in the lunar cycle over centuries
lunar_orbit_correction = (13 + 8 * leap_year_100) // 25

# Step 8: Set century_start to the remainder of 
# (15 - lunar_orbit_correction + leap_year_100 - leap_year_400) divided by 30
# This finds the offset for the start of the lunar cycle in this century
century_start = (15 - lunar_orbit_correction + leap_year_100 - leap_year_400) % 30

# Step 9: Set sunday_offset to the remainder of 
# (4 + leap_year_100 - leap_year_400) divided by 7
# This helps determine which day of the week Easter falls on
sunday_offset = (4 + leap_year_100 - leap_year_400) % 7

# Step 10: Set days_added to the remainder of 
# (19 x lunar_year_cycle_position + century_start) divided by 30
# This calculates days from March 21 to the Paschal full moon
days_added = (19 * lunar_year_cycle_position + century_start) % 30

# Step 11: Set day_of_week_offset to the remainder of 
# (2 x weekday_slide_part_1 + 4 x weekday_slide_part_2 + 6 x days_added + sunday_offset) divided by 7
# This calculates how many days after the full moon the next Sunday occurs
day_of_week_offset = (2 * weekday_slide_part_1 + 4 * weekday_slide_part_2 + 6 * days_added + sunday_offset) % 7

# Step 12: Set total_days_added to 22 + days_added + day_of_week_offset
# 22 represents March 22 (the earliest possible Easter date)
# This gives total days from March 1 to Easter Sunday
total_days_added = 22 + days_added + day_of_week_offset

# Step 13: Set day_of_easter to the remainder of total_days_added divided by 31
# This converts total days to the actual day of the month
day_of_easter = total_days_added % 31

# Step 14: Set month_of_easter to 3 + (total_days_added divided by 31)
# 3 = March, 4 = April. Adding the quotient determines the correct month
month_of_easter = 3 + (total_days_added // 31)

# Step 15: Print the result in the exact format required
# Example: In 2001 Easter Sunday is on 4/15/2001.
print("In", year, "Easter Sunday is on", str(month_of_easter) + "/" + str(day_of_easter) + "/" + str(year) + ".")
