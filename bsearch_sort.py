from random import randint

def binary_search(value, num_list: list):
    resultok = False
    first = 0
    last = len(num_list) - 1
    while resultok != True and first <= last:
        middle = (first + last) // 2
        if value > num_list[middle]:
            first = middle + 1
        elif value < num_list[middle]:
            last = middle - 1
        elif value == num_list[middle]: #or else:
            first = middle
            pos = middle
            last = first
            resultok = True

    if resultok == True:
        return f'Элемент найден! {pos}'
    else:
        return f'Элемент не найден!'

def bubble_sort(bubble_list: list):
    bubbles_len = len(bubble_list)
    for bubbles in range(bubbles_len):
        for bubble in range(0, bubbles_len-bubbles-1):
            if bubble_list[bubble] > bubble_list[bubble + 1]:
                bubble_list[bubble], bubble_list[bubble+1] = bubble_list[bubble+1], bubble_list[bubble]
    return bubble_list


list1 = []
for i in range(20):
    list1.append(randint(-10, 10))
print(bubble_sort(list1))

list2 = bubble_sort(list1)

print(binary_search(0, list2))
print(binary_search(1, list2))

