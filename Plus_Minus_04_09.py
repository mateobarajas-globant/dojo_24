def fractions(arr):
    total_elements = len(arr)
    positive_count = sum(1 for num in arr if num > 0)
    negative_count = sum(1 for num in arr if num < 0)
    zero_count = sum(1 for num in arr if num == 0)
    
    positive_fraction = positive_count / total_elements
    negative_fraction = negative_count / total_elements
    zero_fraction = zero_count / total_elements
    
    print("{:.6f}".format(positive_fraction))
    print("{:.6f}".format(negative_fraction))
    print("{:.6f}".format(zero_fraction))

arr = [-4, 3, -9, 0, 4, 1]
fractions(arr)