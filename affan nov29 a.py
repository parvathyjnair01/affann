"""Program to check whether the given number is a valid mobile number or not using functions.

Rules:

   1 Every number should contain exactly 10 digits.
   2 The first digit should be 7 or 8 or 9
"""

def valid_mobile(number):
    if len(number)==10 and number[0] in ["7","8","9"]:
        return True
    return False
mobile=input("enter number")
if valid_mobile(mobile):
        print("valid")
else:
        print("in valid")