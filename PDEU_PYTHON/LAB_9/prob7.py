def ispalindrome(s):
    s = ''.join(s.lower().split())
    return s == s[::-1]

print(ispalindrome("A man a plan a canal Panama"))  
print(ispalindrome("Hello"))  

# Output :
# True
# False