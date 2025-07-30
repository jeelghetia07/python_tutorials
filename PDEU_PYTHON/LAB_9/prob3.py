def create_array(x, y, z, value):
    array = []
    
    for i in range(x):
        layer = [] 
        for j in range(y):
            row = [] 
            for k in range(z):
                row.append(value) 
            layer.append(row) 
        array.append(layer) 
    
    return array 

array_3d = create_array(3, 4, 4, 5) 

for i in range(len(array_3d)):
    print(f"Layer {i + 1}:")
    for row in array_3d[i]:
        print(row)
    print()
