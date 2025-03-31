def verbing(word):
    if len(word) < 3:
        return word
    elif word.endswith('ing'):
        return word + 'ly'  # מחליפים 'ing' ב-'ly'
    else:
        return word + 'ing'


print(verbing('walk'))      # Expected output: walking
print(verbing('swimming'))  # Expected output: swimmingly
print(verbing('do'))        # Expected output: do


"""
To complete this exercise:
--------------------------
No any implementation notes. 


Exercise Breakdown:
-------------------
The `endswith()` method to determine if the word ends with 'ing'.
"""