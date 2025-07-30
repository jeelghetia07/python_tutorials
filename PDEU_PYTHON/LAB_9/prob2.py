def compute(n):
    n1 = int(str(n))      
    n2 = int(str(n) * 2)  
    n3 = int(str(n) * 3)  
    n4 = int(str(n) * 4)  
    
    return n1 + n2 + n3 + n4  

for num in range(4, 8):
    print(f"compute({num}) = {compute(num)}")

#Output : 
# compute(4) = 4936
# compute(5) = 6170
# compute(6) = 7404
# compute(7) = 8638
