print("Enter -1 for absent ")

s1 = int(input("Enter marks of sub-1 : "))
s2 = int(input("Enter marks of sub-2 : "))
s3 = int(input("Enter marks of sub-3 : "))

print("\t--Result--")

total = s1+s2+s3
avg = total/3

print("Total obtained marks:",total)
print("Average of the marks:",round(avg,2))
print("Grade of subject 1:",end=" ")
if (0<=s1<=39):
    print("F")
elif (40<=s1<=44):
    print("P")
elif (40<=s1<=44):
    print("P")
elif (45<=s1<=49):
    print("C")
elif (50<=s1<=54):
    print("B")
elif (55<=s1<=59):
    print("B+")
elif (60<=s1<=69):
    print("A")
elif (70<=s1<=79):
    print("A+")
elif (80<=s1<=100):
    print("O")
else:
    print("NA")

print("Grade of subject 2:",end=" ")

if (0<=s2<=39):
    print("F")
elif (40<=s2<=44):
    print("P")
elif (40<=s2<=44):
    print("P")
elif (45<=s2<=49):
    print("C")
elif (50<=s2<=54):
    print("B")
elif (55<=s2<=59):
    print("B+")
elif (60<=s2<=69):
    print("A")
elif (70<=s2<=79):
    print("A+")
elif (80<=s2<=100):
    print("O")
else:
    print("NA")

print("Grade of subject 3:",end=" ")

if (0<=s3<=39):
    print("F")
elif (40<=s3<=44):
    print("P")
elif (40<=s3<=44):
    print("P")
elif (45<=s3<=49):
    print("C")
elif (50<=s3<=54):
    print("B")
elif (55<=s3<=59):
    print("B+")
elif (60<=s3<=69):
    print("A")
elif (70<=s3<=79):
    print("A+")
elif (80<=s3<=100):
    print("O")
else:
    print("NA")

print("Final Grade:",end=" ")

if (0<=avg<=39):
    print("F")
elif (40<=avg<=44):
    print("P")
elif (40<=avg<=44):
    print("P")
elif (45<=avg<=49):
    print("C")
elif (50<=avg<=54):
    print("B")
elif (55<=avg<=59):
    print("B+")
elif (60<=avg<=69):
    print("A")
elif (70<=avg<=79):
    print("A+")
elif (80<=avg<=100):
    print("O")
else:
    print("NA")

# Output :
# Enter -1 for absent 
# Enter marks of sub-1 : 95
# Enter marks of sub-2 : 89
# Enter marks of sub-3 : 97
#         --Result--
# Total obtained marks: 281
# Average of the marks: 93.67
# Grade of subject 1: O
# Grade of subject 2: O
# Grade of subject 3: O
# Final Grade: O