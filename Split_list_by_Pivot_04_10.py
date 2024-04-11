def split_list_by_pivot(list, pivot):
    if not list:
        return [[], []]
    
    smaller, greater = split_list_by_pivot(list[1:], pivot)
    
    if list[0] < pivot:
        smaller.append(list[0])
    else:
        greater.append(list[0])
    return [smaller, greater]

numbers = [2,7,8,3,1,4]
pivot = 4
result = split_list_by_pivot(numbers, pivot)
print(result[0],",",result[1])