prices = {
    "rice": 50,
    "wheat": 40,
    "sugar": 30,
    "milk": 25
}

quantities = {
    "rice": 2,    
    "wheat": 3,   
    "sugar": 1,   
    "milk": 4     
}

total_bill = 0

for item in prices:
    if item in quantities:
        total_bill += prices[item] * quantities[item]

print("Total Bill: ₹", total_bill)

# Output:
# Total Bill: ₹ 385