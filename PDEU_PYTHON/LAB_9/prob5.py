def ispangram(s):
    s = s.lower()
    alphaset = set('abcdefghijklmnopqrstuvwxyz')
    return alphaset <= set(s)

print(ispangram("The quick brown fox jumps over the lazy dog"))  
print(ispangram("Crazy Fredrick bought many very exquisite opal jewels"))  

# Output :
# True
# True