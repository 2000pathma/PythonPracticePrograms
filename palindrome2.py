#Python program to check if a string is palindrome or not
# function to check string is
# palindrome or not
def isPalindrome(s): 
    # Using predeﬁned function to
    # reverse to stringprint(s)
    rev = ''.join(reversed(s)) 
    # Checking if both string are equal or not
    if (s == rev):
        print("yes")
    else:
        print("no")
# main function
s = "malayalam"
ans = isPalindrome(s) 
