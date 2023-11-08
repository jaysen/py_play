# a function to check if a string is a palindrome (case insensitive)
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

