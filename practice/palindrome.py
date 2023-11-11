# a function to check if a string is a palindrome (case-insensitive)
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]


# test it out:
print(is_palindrome('racecar'))
print(is_palindrome('Racecar'))
print(is_palindrome('Racecar!'))
print(is_palindrome('MoMom'))
print(is_palindrome('MMoooooomm'))
