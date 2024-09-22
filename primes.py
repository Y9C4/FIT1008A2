from data_structures.referential_array import ArrayR

array = ArrayR(5)
fillers = [1,2,1,3,5]

for i in range(len(fillers)):
    array[i] = fillers[i]

def count_in(array, key) -> int:
    count = 0
    for i in array:
        if i == key:
            count+=1
    return count

print(count_in(array, 1))