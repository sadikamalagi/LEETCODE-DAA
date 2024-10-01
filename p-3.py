
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def fractional_knapsack(W, items, N):
    
    items.sort(key=lambda x: (x.value / x.weight), reverse=True)

    total_value = 0.0  
   
    for i in range(N):
       
        if items[i].weight <= W:
            W -= items[i].weight
            total_value += items[i].value
       
        else:
            total_value += items[i].value * (W / items[i].weight)
            break  
    return total_value


if __name__ == "__main__":
    
    items = [
        Item(60, 10),
        Item(100, 20),
        Item(120, 30)
    ]
    W = 50 
    N = len(items)  
    
    max_value = fractional_knapsack(W, items, N)
    print(f"Maximum value in Knapsack = {max_value}")
