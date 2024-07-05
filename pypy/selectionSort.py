def selection_sort(list):
    for i in range(len(list) - 1):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list

#test it here!!
list = [10,9,8,7,6,5,4,3,2,1]
sorted_list = selection_sort(list)
print("The sorted list is", sorted_list)