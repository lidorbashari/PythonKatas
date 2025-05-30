def get_century(year):
    expected_year = int(year / 100)
    if year % 100 != 0:
        expected_year += 1
        return expected_year
    return expected_year

    """
    Returns the century of the given year.
    """
    # Implement the function to return the correct century.


result = get_century(1786)
print(result)  # 18 expected

result = get_century(1905)
print(result)  # 20 expected

result = get_century(2000)
print(result)  # 20 expected

result = get_century(2023)
print(result)  # 21 expected


"""
To complete this exercise:
--------------------------
Implement the 'get_century' function to return the correct century for the given year.
For example, the year 1786 is in the 18th century, and the year 2023 is in the 21st century.


Exercise Breakdown:
-------------------
Understanding the // operator will help you solve this exercise.
"""
