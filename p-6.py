def maximumUnits(boxTypes, truckSize):
    
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    
    total_units = 0 
    for numberOfBoxes, numberOfUnitsPerBox in boxTypes:
        
        boxes_to_take = min(truckSize, numberOfBoxes)
        
       
        total_units += boxes_to_take * numberOfUnitsPerBox
        
        
        truckSize -= boxes_to_take
        
       
        if truckSize == 0:
            break
    
    return total_units


if __name__ == "__main__":
    
    boxTypes = [[1, 3], [2, 2], [3, 1]]
    truckSize = 4
    
   
    result = maximumUnits(boxTypes, truckSize)
    
    print(f"Maximum units on the truck: {result}")
