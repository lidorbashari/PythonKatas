def reformat_phone(phone_str):
    digits = ''
    for char in phone_str:
        if char.isdigit():
            digits += char
    if len(digits) != 10:
        return None
    return f'({digits[0:3]}) {digits[3:6]}-{digits[6:10]}'
    """
    This function takes a string representing a phone number and reformats it into
    a standardized format: (XXX) XXX-XXXX, where X represents a digit.
    The function removes any non-numeric characters from the string and reformats it.

    Return None if the input is invalid (not exactly 10 digits)
    """


print(reformat_phone("123-456-7890"))  # Expected output: (123) 456-7890
print(reformat_phone("(123) 456-7890"))  # Expected output: (123) 456-7890
print(reformat_phone("1234567890"))  # Expected output: (123) 456-7890
print(reformat_phone("123-458//-9/4/8++"))  # Expected output: None


"""
To complete this exercise:
--------------------------
No any implementation notes. 


Exercise Breakdown:
-------------------
The `isdigit()` can help you to filter out non-numeric characters.
"""
