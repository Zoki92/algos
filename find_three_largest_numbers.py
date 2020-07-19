"""Write a function that takes an array and without sorting the input array returns a sorted array of 
the three largest integers in the array.
[10, 5, 9, 10, 12]
returns
[10, 10, 12]
"""

def find_numbers(array):
    largest = []
    for num in array:
        print(largest)
        if len(largest) >= 3:
            if largest[2] <= num:
                largest.append(num)
                largest.pop(0)
            elif largest[1] <= num:
                largest.insert(2, num)
                largest.pop(0)
            elif largest[0] <= num:
                largest.pop(0)
                largest.insert(0, num)
            else:
                pass
                
        elif len(largest) == 2:
            if largest[1] < num:
                largest.append(num)
            elif largest[0] < num:
                largest.insert(1, num)
            else:
                largest.insert(0, num)
        elif len(largest) == 1:
            if largest[0] < num:
                largest.append(num)
            else:
                largest.insert(0, num)
        else:
            largest.append(num)
    return largest
        
test = [10, 5, 9, 10, 12]
test2 = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
test3 = [55, 43, 11, 3, -3, 10]
# print(find_numbers(test))
# print(find_numbers(test2))
print(find_numbers(test3))