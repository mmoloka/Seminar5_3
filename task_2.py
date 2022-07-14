# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

def SearchList(arr, num):
    if str(num) in arr:
        return 'yes'
    return 'no'


list1 = ['hello', '12', 'red', '657']
print(SearchList(list1, 657))
