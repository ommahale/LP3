def fractional_knapsack(value, weight, capacity):
    n = len(value)
    ratios = [(v/w,v,w) for v,w in zip(value,weight)]
    ratios.sort(reverse = True)
    
    max_value = 0
    knapsack = []
    
    for ratio,v,w in ratios:
        if w<=capacity:
            max_value += v
            knapsack.append((v,w,1))
            capacity -= w
            
        else:
            fraction = capacity / w
            max_value += v * fraction
            knapsack.append((v, w, fraction))
            break

    return max_value, knapsack
    
n = int(input("Enter the number of items: "))
value = []
weight =[]
for i in range(n):
    v,w = map(int, input(f"Enter value and weight for {i+1} space separated: ").split())
    value.append(v)
    weight.append(w)
capacity = int(input("Enter capacity"))
    
max_value, knapsack = fractional_knapsack(value, weight, capacity)

print("Maximum value in the knapsack:", max_value)
print("Selected items in the knapsack:", knapsack)
            
            
        
