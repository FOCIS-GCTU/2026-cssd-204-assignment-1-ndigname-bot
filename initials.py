# File: easter_date.py
# Description: This program calculates the date of Easter Sunday for any year given
#               using the (Computus algorithm) developed by Carl Friedrich Gauss.
# Assignment Number: 3
#
# Name:Emmanuel Ndignam Nelimo
# SID:2425401719
# Email:2425401719@live.gctu.edu.gh
# Grader: MR.AUGUSTUS BUCKMAN
# Slip days used this assignment: 0
#
# On my honor, Emmanuel Ndignam Nelimo, this programming assignment is my own work
# and I have not provided this code to any other student.


def main():
    # Ask the user for the year and save it in a variable named year
    year = int(input("Enter year: "))

    # Divide year by 19 and call the remainder lunar_year_cycle_position
    lunar_year_cycle_position = year % 19

    # Divide year by 4 and call the remainder weekday_slide_part_1
    weekday_slide_part_1 = year % 4

    # Divide year by 7 and call the remainder weekday_slide_part_2
    weekday_slide_part_2 = year % 7

    # Divide year by 100 and call the quotient leap_year_100
    leap_year_100 = year // 100

    # Divide leap_year_100 by 4 and call the quotient leap_year_400
    leap_year_400 = leap_year_100 // 4

    # Set lunar_orbit_correction to (13 + 8 x leap_year_100) divided by 25
    lunar_orbit_correction = (13 + 8 * leap_year_100) // 25

    # Set century_start to the remainder of (15 - lunar_orbit_correction + leap_year_100 - leap_year_400) divided by 30
    century_start = (15 - lunar_orbit_correction + leap_year_100 - leap_year_400) % 30

    # Set sunday_offset to the remainder of (4 + leap_year_100 - leap_year_400) divided by 7
    sunday_offset = (4 + leap_year_100 - leap_year_400) % 7

    # Set days_added to the remainder of (19 x lunar_year_cycle_position + century_start) divided by 30
    days_added = (19 * lunar_year_cycle_position + century_start) % 30

    # Set day_of_week_offset to the remainder of (2 x weekday_slide_part_1 + 4 x weekday_slide_part_2 + 6 x days_added + sunday_offset) divided by 7
    day_of_week_offset = (2 * weekday_slide_part_1 + 4 * weekday_slide_part_2 + 6 * days_added + sunday_offset) % 7

    # Set total_days_added to 22 + days_added + day_of_week_offset
    total_days_added = 22 + days_added + day_of_week_offset

    # Set day_of_easter to the remainder of total_days_added divided by 31
    day_of_easter = total_days_added % 31

    # Set month_of_easter to 3 + (total_days_added divided by 31)
    month_of_easter = 3 + (total_days_added // 31)

    # Print the date of Easter Sunday in the required format
    print("In " + str(year) + " Easter Sunday is on " + str(month_of_easter) + "/" + str(day_of_easter) + "/" + str(year) + ".")


if __name__ == "__main__":
    main()
