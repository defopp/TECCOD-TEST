# 1. Написать функцию, 
# которая принимает на вход список целых чисел и возвращает новый список, 
# содержащий только уникальные элементы из исходного списка.
def uniqe_list(int_list) -> list:
    return list(set(int_list))

print(uniqe_list([1,2,2,3,45,6,7,1,1,1,1,1,-1,-100000,-100000,-100000]))







