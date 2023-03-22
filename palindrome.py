# Python program to check if a string is palindrome or not
# function which return reverse of a string 
def isPalindrome(s):
    return s == s[::-1]
s =input("input:")
ans = isPalindrome(s)
if ans:
    print("Yes")
else:
    print("No")
